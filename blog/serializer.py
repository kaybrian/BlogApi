from rest_framework import serializers 
from .models import Blog


class BlogSerializer(serializers.ModelSerializers):
    class Meta:
        model = Blog
        fields = "__all__"