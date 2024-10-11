# 7. Django Rest Framework Generics RetrieveAPIView 
# from webbrowser import get
from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from .serializers import ProductSerializer
# for function based views 
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from django.shortcuts import get_list_or_404
# from django.http import Http404
from api.authentication import TokenAuthentication


""" SESSION ONE """
# views
# # confusing to work with 
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         # print(serializer)
#         # serializer.save()
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)


# # to get from the models
# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = 'pk'  # Use 'id' field as the URL parameter


# """ 11. the UpdateAPIView & DestroyAPIView are very similar to the ProductDetailAPIView """
# class ProductUpdateAPIView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'  # Use 'id' field as the URL parameter

#     def perform_update(self, serializer):
#         instance = serializer.save()
#         if not instance.content:
#             instance.content = instance.title
#             ## 

# # delete 
# class ProductDeleteAPIView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     def perform_destroy(self, instance):
#         super().perform_destroy(instance)

# # product_delete_view = ProductDeleteAPIView.as_view()

# # to post to model
# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         # print(serializer)
#         # serializer.save()
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)


# # Dont use this 
# # class ProductListAPIView(generics.ListAPIView):
# #     """NOT USE"""
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer



# """12. Mixins and a Generic API View"""
# class ProductMixinView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     look_up = "pk" 

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrive(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def perform_create(self, serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = "This is a row's content."
#         serializer.save(content=content)


# product_mixin_view = ProductMixinView.as_view()


# # # FUNCTION BASED VIEW --- 
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         # get request --> Detail View or List View
#         if pk is not None:
#             # detail view 
#             # queryset = Product.objects.filter(pk=pk)
#             # if not queryset.exists():
#             #     raise Http404
#             """OR"""
#             obj = get_list_or_404(Product, pk=pk) 
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)

#         # list view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == "POST":
#         # post request --> Create an item
#         # pass
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"Invalid":"Not good data"}, status = 400)
    

""" SESSION TWO """
# # authentication AND permissions
# # 
# # custom permissions 
# from .permissions import IsStaffEditorPermission

# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes = [authentication.SessionAuthentication]
#     # permission_classes = [permissions.IsAuthenticated] # Not working yet, class changed to classes
#     # permission_classes = [permissions.DjangoModelPermissions] # User permission
#     permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] # Custom Permissions


#     def perform_create(self, serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)


# class ProductUpdateAPIView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = 'pk'

#     def perform_update(self, serializer):
#         instance = serializer.save()
#         if not instance.content:
#             instance.content = instance.title
#             ## 

# 2th Oct. 2024 
"Token Authentication"
from .permissions import IsStaffEditorPermission

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication, 
        # authentication.TokenAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] # Custom Permissions
    
     
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            ## 


