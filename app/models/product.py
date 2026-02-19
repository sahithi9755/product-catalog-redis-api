import uuid
from sqlalchemy import Column, String, Float, Integer
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)