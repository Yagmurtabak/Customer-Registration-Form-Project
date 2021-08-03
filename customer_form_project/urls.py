"""customer_form_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from core.views import register
from core.views import customerCreateView, customerListView,customerDetailView,customerDeleteView,customerUpdateView,RegisterView
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name="register"),   
    path('',customerListView.as_view()),
    path('detail/<int:pk>', customerDetailView.as_view(), name="detail"),
    path('update/<int:pk>/', customerUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/',  customerDeleteView.as_view(),name="delete"),
    path('create', customerCreateView.as_view(), name="create"),
    path('registerate', RegisterView.as_view(), name= "registerate"),
    path('register/', register, name="register"),
    path('login/' , authViews.LoginView.as_view()),
]
