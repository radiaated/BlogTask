from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from .serializers import BlogSerializer
from datetime import date
from auths.serializers import is_loggedin

# Create your views here.

@api_view(["GET"])
def blog_list(request):
    
    blogs = Blog.objects.all()

    serializers = BlogSerializer(blogs, many=True)

    return Response(serializers.data)


@api_view(["GET"])
def user_blogs(request, id):
    print(id)
    blogs = Blog.objects.filter(user__id = id)

    serializers = BlogSerializer(blogs, many=True)

    return Response(serializers.data)


# @authentication_classes(IsAuthenticated)
@api_view(["POST"])
@is_loggedin
def create_blog(request):
    print(request.COOKIES)
    user = request.user
    print(user)

    if request.method == "POST":
        post_data = request.data



        blog = Blog.objects.create(
            title=post_data['title'],
            description=post_data['description'],
            user=user
        )

        if blog:
            blog.save()

        serializers = BlogSerializer(blog)

        return Response(serializers.data)
    
    
    


@authentication_classes(IsAuthenticated)
@api_view(["PUT", "DELETE"])
def blog_item(request, id):
    user = request.user
   
    
    if request.method == "PUT":
        put_data = request.data

        blog = Blog.objects.get(id = id, user=user)
        
        if put_data.get("title"):
            blog.title = put_data['title']
        
        if put_data.get("description"):
            blog.description = put_data['description']

        if blog:
            blog.updated_date = date.today()
            blog.save()

        serializers = BlogSerializer(blog)

        return Response(serializers.data)
    
    elif request.method == "DELETE":

        blog = Blog.objects.get(id = id, user=user).delete()

        return Response({"detail": "Deleted succesfully."})
    
@api_view(["GET"])
def view_blog(request, id):

    
    blog = Blog.objects.get(id = id)

    serializers = BlogSerializer(blog)

    return Response(serializers.data)
    
    