import pytest
from fastapi.testclient import TestClient
from solution.main import app
from solution.db_details.tools import SessionLocal


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    db = SessionLocal()
    db.execute("DELETE FROM stores;")
    db.execute("DELETE FROM products;")
    db.commit()
    yield
    db.execute("DELETE FROM products;")
    db.commit()
    db.close()


@pytest.fixture
def client():
    return TestClient(app)


def test_create_store(client):
    new_store = {
        "store_name": "store_111",
    }
    response = client.post("/api/store", json=new_store)
    assert response.status_code == 200
    assert response.json() == new_store


def test_create_product(client):
    store_data = {"store_name": "store_111"}
    new_store_response = client.post("/api/store", json=store_data)

    new_product = {
        "store_name": new_store_response.json()["store_name"],
        "name": "product_111",
        "price": 111.0
    }
    response = client.post("/api/product", json=new_product)
    response_data = response.json()

    assert 'id' in response_data
    assert response_data['store_name'] == new_product['store_name']
    assert response_data['name'] == new_product['name']
    assert response_data['price'] == new_product['price']


def test_read_products_by_name(client):
    name_contains = "111"
    response = client.get(f"/api/products-by-name?name_contains={name_contains}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
