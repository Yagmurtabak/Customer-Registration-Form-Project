from django.urls import path

from core.views import customerCreateView, customerListView,customerDetailView,customerDeleteView,customerUpdateView,RegisterView
from core.views import register
from django.contrib.auth import views as authViews

urlpatterns = [
    path('',customerListView.as_view(), name="list"),
    path('detail/<int:pk>', customerDetailView.as_view(), name="detail"),
    path('update/<int:pk>/', customerUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/',  customerDeleteView.as_view(),name="delete"),
    path('create', customerCreateView.as_view(), name="create"),
    path('registerate', RegisterView.as_view(), name= "registerate"),
    path('register/', register, name="register"),
    path('login/' , authViews.LoginView.as_view()),
    
]