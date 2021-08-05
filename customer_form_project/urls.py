from django.contrib import admin
from django.urls import path, include

from core.views import (
    CustomerCreateView, 
    CustomerListView, 
    CustomerDetailView,
    RegisterationView
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
     path('register/', RegisterationView.as_view(), name = "register"),   
    path('', CustomerListView.as_view()),
    path('create', CustomerCreateView.as_view(), name="create"),
    path('detail/<int:pk>/', CustomerDetailView.as_view(), name="detail"),

]
