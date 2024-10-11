from django.urls import path 

from . views import ( 
    # ProductDetailAPIView, 
    # ProductCreateAPIView, 
    # ProductListAPIView, 
    ProductListCreateAPIView, 
    # product_alt_view, 
    # ProductUpdateAPIView,
    # product_delete_view,
    # ProductDeleteAPIView,
    # product_mixin_view
    )

urlpatterns = [
    # Generics
    path('', ProductListCreateAPIView.as_view()),
    # path('<int:pk>', ProductDetailAPIView.as_view()),
    # path('', ProductCreateAPIView.as_view()),
    # path('', ProductListAPIView.as_view()),

    # # Update and delete 
    # path('<int:pk>/update/', ProductUpdateAPIView.as_view()),
    # path('<int:pk>/delete/', ProductDeleteAPIView.as_view()),

    # # mixins 
    # path('', product_mixin_view),

    # # from the function based view 
    # path('', product_alt_view),
    # path('<int:pk>', product_alt_view),
]