from django.urls import path
from users import views

urlpatterns = [
    path('users',views.Users_List),
    path('users/<int:pk>',views.Users_Detail)
]