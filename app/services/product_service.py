from sqlalchemy.orm import Session
from app.models.product import Product
from app.services.cache_service import (
    get_product_from_cache,
    set_product_in_cache,
    invalidate_product_cache,
)


def get_product(db: Session, product_id: str):
    # 🔍 1. Check cache
    cached = get_product_from_cache(product_id)
    if cached:
        return cached

    # 🗄️ 2. Fetch from DB
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None

    product_dict = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock_quantity": product.stock_quantity,
    }

    # 💾 3. Store in cache
    set_product_in_cache(product_dict)

    return product_dict


def create_product(db: Session, data: dict):
    product = Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product_id: str, data: dict):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None

    for key, value in data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    # ❌ invalidate cache
    invalidate_product_cache(product_id)

    return product


def delete_product(db: Session, product_id: str):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return False

    db.delete(product)
    db.commit()

    # ❌ invalidate cache
    invalidate_product_cache(product_id)

    return True