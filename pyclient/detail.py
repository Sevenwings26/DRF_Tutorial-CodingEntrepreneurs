import requests

filepath = "C:/TEACHING_RESTFRAMEWORK/coding-enterp/tutorialsteps.txt"
# mode="x" # to create file 
# mode="w" # to write into existing file 
# with open(filepath, mode="w") as file_obj:
#     file_obj.write("""
#                    CodingEntrepreneurs (Youtube) teaching steps
#         1.  
#         2.
#         3.
#         4i. Django Models (GET data from models, using JsonResponse)
#         4ii. Django Models (GET Data from models, using Rest Framework View & Response)
#         5.  Django Rest Framework Model Serializers       
#         6. POST - Insert data with Djangi Rest Framework views
#         7. Django Rest Framework Generics RetrieveAPIView 
#         8. Django Rest Framework Generics CreateAPIView 
#  """)
    
# from the products app --- views and urls(collects pk value)

endpoint = "http://127.0.0.1:8000/api/products/1"
# GET 
get_response = requests.get(endpoint)

try:
    data = get_response.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print("Response is not in JSON format:", get_response.status_code)

