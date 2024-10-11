
import requests



# endpoint = "http://127.0.0.1:8000/api/products/"
endpoint = "http://127.0.0.1:8000/api/auth/"
get_response = requests.post(endpoint, json={'username':'rest_admin'})
print(get_response.json())

endpoint = "http://127.0.0.1:8000/"
get_response = requests.get(endpoint)
try:
    data = get_response.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print("The response is not valid JSON")
    # print(get_response.text)  # Print the raw response
