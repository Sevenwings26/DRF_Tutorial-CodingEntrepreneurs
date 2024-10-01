import requests

product_id = int(input("Enter product id: "))
try:
    product_id = int(product_id)
    print(f'{product_id} --- Converted to integer...')
except:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = "http://127.0.0.1:8000/api/products/{product_id}/delete/"
    get_response = requests.get(endpoint)
    # print(get_response.status_code, get_response.status_code==204)
    print(get_response.json())