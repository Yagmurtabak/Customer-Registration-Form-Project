from django.urls import path
from django.contrib.auth.views  import LoginView, LogoutView

from core.views import (
    CustomerCreateView, 
    CustomerListView, 
    CustomerDetailView, 
    CustomerDeleteView, 
    CustomerUpdateView, 
    CustomerView,
    RegisterationView
    )


urlpatterns = [
    path('', CustomerListView.as_view(), name = "list"),
    path('detail/<int:pk>/', CustomerDetailView.as_view(), name = "detail"),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name = "update"),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name = "delete"),
    path('create', CustomerCreateView.as_view(), name = "create"),
    path('customer', CustomerView.as_view(), name = "customer"),
    path('register/', RegisterationView.as_view(), name = "register"),
    path('login/', LoginView.as_view()),
    path('logout/',LogoutView.as_view(), name = "logout"),
]
