from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.home , name='home'),
    path('view-blog-list/',views.ViewBlogs,name='view-blog-list'),
    path('create-blog/',views.CreateBlogs,name='create-blog'),
    path('update-blog/<str:pk>/',views.UpdateBlogs,name='update-blog'),
    path('view-blog-detail/<str:pk>/',views.BlogDetails,name='view-blog-detail'),
    path('delete-blog/<str:pk>/',views.DeleteBlogs,name='delete-blog'),
]
