from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services import product_service

router = APIRouter(prefix="/products")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", status_code=201)
def create_product(payload: dict, db: Session = Depends(get_db)):
    return product_service.create_product(db, payload)


@router.get("/{product_id}")
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = product_service.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{product_id}")
def update_product(product_id: str, payload: dict, db: Session = Depends(get_db)):
    product = product_service.update_product(db, product_id, payload)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: str, db: Session = Depends(get_db)):
    success = product_service.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")