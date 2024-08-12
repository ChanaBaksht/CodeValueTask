from solution.db_details.models import StoreModel, ProductModel
from sqlalchemy.orm import Session
from solution.db_details.schemas import StoreSchema, ProductSchema
from solution.db_details.tools import with_db_session
from sqlalchemy import func


class StoresManager:

    @with_db_session
    def create_store(self, new_store: StoreModel, session: Session):
        store = StoreSchema(**new_store.dict())
        session.add(store)
        session.commit()
        session.refresh(store)
        return store

    @with_db_session
    def read_stores(self, session: Session):
        return session.query(StoreSchema).all()

    @with_db_session
    def create_product(self, new_product: ProductModel, session: Session):
        product = ProductSchema(**new_product.dict())
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    @with_db_session
    def read_products(self, session: Session):
        return session.query(ProductSchema).all()

    @staticmethod
    def convert_db_models_to_out_models(product_rows: list[ProductSchema]) -> list[ProductModel]:
        return [ProductModel.from_orm(product_row) for product_row in product_rows]

    @with_db_session
    def read_products_by_name(self, name_contains: str, session: Session) -> list[ProductModel]:
        rows = (session.query(ProductSchema)
                .filter(func.lower(ProductSchema.name).contains(func.lower(name_contains))).all())
        return self.convert_db_models_to_out_models(rows)
