from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.home , name='home'),
    path('view-blog-list/',views.ViewBlogs,name='view-blog-list'),
    path('create-blog/',views.CreateBlogs,name='create-blog')
]
