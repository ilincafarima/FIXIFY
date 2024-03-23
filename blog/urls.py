from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # URL pattern for listing blog posts
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),  # URL pattern for viewing a specific blog post
]
