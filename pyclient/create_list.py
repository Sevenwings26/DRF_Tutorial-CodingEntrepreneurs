filepath = "C:/TEACHING_RESTFRAMEWORK/coding-enterp/tutorialsteps.txt"
# mode="x" # to create file 
# mode="w" # to write into existing file 
with open(filepath, mode="a") as file_obj:
    file_obj.write(""" 
        9. Django Rest Framework Generics ListAPIView & ListCreateAPIView 
 """)


import requests
    
# from the products app --- views and urls(collects pk value)

endpoint = "http://127.0.0.1:8000/api/products/"
# # GET 
# get_response = requests.post(endpoint, json={'title':'This is a field...'})
# # get_response = requests.post(endpoint)
# try:
#     data = get_response.json()
#     print(data)
# except requests.exceptions.JSONDecodeError:
#     print("Response is not in JSON format:", get_response.status_code)


# LsitCreateAPIView 
get_response = requests.get(endpoint)
print(get_response.json())