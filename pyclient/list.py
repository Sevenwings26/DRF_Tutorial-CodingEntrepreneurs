
import requests
    
endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.get(endpoint)
try:
    data = get_response.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print("The response is not valid JSON")
    print(get_response.text)  # Print the raw response
