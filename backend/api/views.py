from django.http import JsonResponse, HttpResponse
from products.models import Product
import json


"""lesson 4 - Fetching data from models, using JsonResponse"""
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     if model_data:
#         data = {
#             'id': model_data.id,
#             'title': model_data.title,
#             'content': model_data.content,
#             'price': model_data.price,
#         }
#     else:
#         data = {'message': 'No product found'}
#     return JsonResponse(data)

# Converting Django model instance into a dictionary 
from django.forms.models import model_to_dict
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # model instance into dictionary
#         data=model_to_dict(model_data, fields={'id','title','content'})
#     return JsonResponse(data)
        
        # using HttpResponse - It send strings not dict
        # json_data_str = json.dumps(data)
    
    # return HttpResponse(json_data_str, headers={"content-type":"application/json"})


"""lesson 5 = Fetching Data from models with Rest Framework View & Response"""
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View...
#     """
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # model instance into dictionary
#         data=model_to_dict(model_data, fields={'id','title','content','price','sale_price'})
#         # note: sale_price is a property(method), it will be sent to the api
#         # instance of the class will need to be created, using the serializers. 
#     else:
#         data = {"message":"None"}
#     return Response(data)

"""# Using Serialzers """
# from products.serializers import ProductSerializer
# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View...
#     """
#     instance = Product.objects.all().order_by("?").first()
#     # instance = Product.objects.all()
#     data = {}
#     if instance:
#         # # model instance into dictionary
#         # data=model_to_dict(model_data, fields={'id','title','content','price','sale_price'})
#         data = ProductSerializer(instance).data
#     else:
#         data = {"message":"None"}
#     return Response(data)


""" POST to api without serializers """
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View...
    """
    data = request.data
    return Response(data)


""" POST to api with serializers """
from products.serializers import ProductSerializer
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View...
    """
    # data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.save()
        # print(serializer.data)
        data = serializer.data
        # print(data)
    return Response(data)