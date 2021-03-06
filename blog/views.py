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
        'Delete':'/delete-blog/<str:pk>/',
        'View-blogs':'/view-blog-list/',
        'View-blog Details':'/view-blog-detail/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def ViewBlogs(request):
    blogs = Blog.objects.all()
    serialiser = BlogSerializer(blogs, many=True)
    return Response(serialiser.data)

@api_view(['POST'])
def CreateBlogs(request):
    serialiser = BlogSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['POST'])
def UpdateBlogs(request,pk):
    blog = Blog.objects.get(id=pk)
    serialiser = BlogSerializer(instance=blog, data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)


@api_view(['GET'])
def BlogDetails(request,pk):
    blog = Blog.objects.get(id=pk)
    serialiser = BlogSerializer(blog,many=False)
    return Response(serialiser.data)

@api_view(['DELETE'])
def DeleteBlogs(request,pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return Response('The blog was deleted Successfully')