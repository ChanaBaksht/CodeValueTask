from pydantic import BaseModel


class StoreModel(BaseModel):
    store_name: str


class ProductModel(BaseModel):
    store_name: str
    name: str
    price: float

    class Config:
        from_attributes = True
