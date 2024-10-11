# filepath = "C:/TEACHING_RESTFRAMEWORK/coding-enterp/tutorialsteps.txt"
# # mode="x" # to create file 
# # mode="w" # to write into existing file 
# with open(filepath, mode="a") as file_obj:
#     file_obj.write(""" 
#         9. Django Rest Framework Generics ListAPIView & ListCreateAPIView 
#  """)


import requests
from getpass import getpass

# 11th Oct. 2024...
# tokenauthentication 
auth_endpoint = "http://127.0.0.1:8000/api/auth/"
userame = input('What is your Username: ')
password = getpass('What is your password: ')

auth_response = requests.post(auth_endpoint, json={"username":userame, 'password':password}),
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization":f'Token {token}',
        '':''
    }

    endpoint = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(endpoint)
    print(get_response)
    

# # from the products app --- views and urls(collects pk value)
# # # GET 
# # get_response = requests.post(endpoint, json={'title':'This is a field...'})
# # # get_response = requests.post(endpoint)
# # try:
# #     data = get_response.json()
# #     print(data)
# # except requests.exceptions.JSONDecodeError:
# #     print("Response is not in JSON format:", get_response.status_code)


# # LsitCreateAPIView 
