from solution.db_details.models import StoreModel, ProductModel
from solution.api_server.controller import StoresController
from solution.api_server.manager import StoresManager
from fastapi import APIRouter

stores_controller = StoresController(stores_manager=StoresManager())

router = APIRouter(tags=["stores"])


@router.post("/store")
def create_store(new_store: StoreModel):
    return stores_controller.create_store(new_store)


@router.get("/stores")
def read_stores():
    return stores_controller.read_stores()


@router.post("/product")
def create_product(new_product: ProductModel):
    return stores_controller.create_product(new_product)


@router.get("/products")
def read_products():
    return stores_controller.read_products()


@router.get("/products-by-name")
async def read_products_by_name(name_contains: str):
    return await stores_controller.read_products_by_name(name_contains)
