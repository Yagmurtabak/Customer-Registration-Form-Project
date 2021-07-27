from django.urls import path

from post.views import *

urlpatterns = [
    path('', postlist_view),
    path('detail/<int:id>', postdetail_view),


    path('update/<int:id>', postupdate_view),
    path('updateYolla/<int:id>', postupdate_view),

    path('delete/<int:id>', postdelete_view),
    path('create', postcreate_view),
    path('newform', newform_view),
]