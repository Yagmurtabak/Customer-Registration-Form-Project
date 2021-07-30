 
from django.urls import path

from post.views import *
from post.views import PostCreateView, PostListView,PostDetailView,PostDeleteView,PostUpdateViev,RegisterView

urlpatterns = [
    path('',PostListView.as_view(), name="list"),
    path('detail/<int:pk>', PostDetailView.as_view(), name="detail"),
    path('update/<int:pk>', PostUpdateViev.as_view(), name="update"),
    path('delete/<int:pk>', PostDeleteView.as_view(),name="delete"),
    path('create', PostCreateView.as_view(), name="create"),
    path('register', RegisterView.as_view(), name= "register"),
]
