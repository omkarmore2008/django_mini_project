from django.urls import path
from products import views

urlpatterns =[
    path('products',views.ProductsList.as_view()),
    path('products/<int:pk>',views.ProductsDetail.as_view())
]