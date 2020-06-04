from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    api_urls = {
        'Create':'/create-blog/',
        'Update':'/update-blog/<str:pk>/',
        'Create':'/create-blog/<str:pk>/',
        'View-blogs':'/view-blog-list/',
    }
    return Response('This is a blog api response',safe=False)