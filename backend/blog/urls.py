from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('create/', csrf_exempt(views.create_blog), name='blog'),
    path('item/<int:id>/', views.blog_item, name='blog-item'),
    path('view/<int:id>/', views.view_blog, name='view-blog'),
    path('list/', views.blog_list, name='blog-list'),
    path('user/<int:id>/', views.user_blogs, name='user-blogs'),
   
]