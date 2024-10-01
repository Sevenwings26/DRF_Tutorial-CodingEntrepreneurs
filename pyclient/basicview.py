# import requests

# endpoint = "http://127.0.0.1:8000/"

# # From models
# get_response = requests.get(endpoint, json={'product':123})  # HTTP request
# print(get_response.json())

""" LESSON NOTE """
# write to a txt file... 
filepath = "C:/TEACHING_RESTFRAMEWORK/coding-enterp/tutorialsteps.txt"
# mode="x" # to create file 
# mode="w" # to write into existing file 
with open(filepath, mode="w") as file_obj:
    file_obj.write("""
                   CodingEntrepreneurs (Youtube) teaching steps
        
                   'VIEWS METHODS & APPROACHES'
        1.  
        2.
        3.
        4i. Django Models (GET data from models, using JsonResponse)
        4ii. Django Models (GET Data from models, using Rest Framework View & Response)
        5.  Django Rest Framework Model Serializers       
        6. POST - Insert data with Djangi Rest Framework views
        7. Django Rest Framework Generics RetrieveAPIView 
        8. Django Rest Framework Generics CreateAPIView 
        9. Django Rest Framework Generics ListAPIView & ListCreateAPIView 
        10. Using Function Based Views For Create Retrieve or List 
    ----------- Generic view over function based view
        11. UpdateAPIView & DestroyAPIView
        12. Mixins and a Generic API View
                   
                'AUTHENTICATION & PERMISSIONS' 
 """)


import requests

endpoint = "http://127.0.0.1:8000/api/"
# GET 
# get_response = requests.get(endpoint)

# try:
#     data = get_response.json()
#     print(data)
# except requests.exceptions.JSONDecodeError:
#     print("Response is not in JSON format:", get_response.status_code)

# POST 
get_response = requests.post(endpoint, json={'title': 'Hello World', 'content':'Ready to serializer'})

try:
    data = get_response.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print("Response is not in JSON format:", get_response.status_code)
