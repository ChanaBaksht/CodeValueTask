import os
import httpx
from solution.db_details.models import ProductModel

STORES_SERVICES_URI = ["EBAY_API_URL", "AMAZON_API_URL"]

STORES_SERVICES = [url for url in map(os.environ.get, STORES_SERVICES_URI) if url]


async def read_products_by_name_from_stores_services(name_contains: str):
    async with httpx.AsyncClient() as client:
        products: list[ProductModel] = []
        for STORE_SERVICE in STORES_SERVICES:
            response = await client.get(f'http://{STORE_SERVICE}/products?name_contains={name_contains}')
            store_products = response.json()
            products.extend([ProductModel(
                store_name=store_products["store"], name=store_product["name"], price=store_product["price"])
                for store_product in store_products["products"]])
        return products
