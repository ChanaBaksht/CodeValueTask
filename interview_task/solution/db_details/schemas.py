from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from solution.db_details.tools import engine

Base = declarative_base()


class StoreSchema(Base):
    __tablename__ = "stores"

    store_name = Column(String(20), primary_key=True, nullable=False, index=True)
    products = relationship("ProductSchema", back_populates="store", cascade="all, delete-orphan")


class ProductSchema(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False, index=True)
    price = Column(Float, nullable=False)
    store_name = Column(String(20), ForeignKey("stores.store_name", ondelete="CASCADE"))
    store = relationship("StoreSchema", back_populates="products")


Base.metadata.create_all(bind=engine)
