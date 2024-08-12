from solution.db_details.models import StoreModel, ProductModel
from solution.api_server.manager import StoresManager
from solution.registered_external_stores.registered_stores import read_products_by_name_from_stores_services


class StoresController:
    def __init__(self, stores_manager: StoresManager):
        self.stores_manager = stores_manager

    def create_store(self, new_store: StoreModel):
        return self.stores_manager.create_store(new_store)

    def read_stores(self):
        return self.stores_manager.read_stores()

    def create_product(self, new_product: ProductModel):
        return self.stores_manager.create_product(new_product)

    def read_products(self):
        return self.stores_manager.read_products()

    async def read_products_by_name(self, name_contains: str):
        products_from_stores_services = await read_products_by_name_from_stores_services(name_contains)
        products_from_registered_stores = self.stores_manager.read_products_by_name(name_contains)
        return products_from_stores_services + products_from_registered_stores
