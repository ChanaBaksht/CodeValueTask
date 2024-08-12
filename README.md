Solution app:

The solution folder contains a FastAPI server that includes the calls indicated below.
This FastAPI router handles store and product management through a set of endpoints that interact with the StoresController.
Here's an overview of the available endpoints:


1. POST /store
    Description: Creates a new store.
    Request Body: Accepts a JSON object based on the StoreModel.
    Response: Returns the created store object.
    Example: { "store_name": "store_111" }

2. GET /stores
    Description: Retrieves a list of all stores.
    Response: Returns a list of store objects.

3. POST /product
    Description: Creates a new product.
    Request Body: Accepts a JSON object based on the ProductModel.
    Response: Returns the created product object.
    Example: { "store_name": "store_111", "name": "product_111", "id": 7, "price": 20.0 }

4. GET /products
    Description: Retrieves a list of all products.
    Response: Returns a list of product objects.

5. GET /products-by-name
   Description: Searches for products by a substring in their name.
   Query Parameter: name_contains - The substring to search for in product names.
   Response: Returns a list of matching product objects.
   Example for name_contains = "111", The Output: [{ "store_name": "store_111", "name": "product_111", "price": 20.0 }]