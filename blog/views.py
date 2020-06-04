from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializer import BlogSerializer
from .models import Blog
# Create your views here.
@api_view(['GET'])
def home(request):
    api_urls = {
        'Create':'/create-blog/',
        'Update':'/update-blog/<str:pk>/',
        'Delete':'/create-blog/<str:pk>/',
        'View-blogs':'/view-blog-list/',
        'View-blog Details':'/view-blog-detail/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def ViewBlogs(request):
    blogs = Blog.objects.all()
    serialiser = BlogSerializer(blogs, many=True)
    return Response(serialiser.data)