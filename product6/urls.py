from django.urls import path
from .views import ProductViewSet, ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, ProductDestroyAPIView, ProductRetrieveUpdateAPIView, ProductListCreateAPIView, ProductRetrieveDestroyAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns=[
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product6/list/', ProductListAPIView.as_view()),
    path('product6/create/', ProductCreateAPIView.as_view()),
    path('product6/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view()),
    path('product6/update/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('product6/destroy/<int:pk>/', ProductDestroyAPIView.as_view()),
    path('product6/retrieve-update/<int:pk>/', ProductRetrieveUpdateAPIView.as_view()),
    path('product6/list-create/', ProductListCreateAPIView.as_view()),
    path('product6/retrieve-destroy/<int:pk>/', ProductRetrieveDestroyAPIView.as_view()),
    path('product6/retrieve-update-destroy/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
]