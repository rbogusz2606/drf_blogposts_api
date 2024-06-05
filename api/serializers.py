from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date", "author"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'password', 'email']