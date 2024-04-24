from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Blog


class BlogSerializer(ModelSerializer):

    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'created_date', 'updated_date', 'username']