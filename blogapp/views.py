
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogCategorySerializer,BlogPostSerializer,BlogCommentSerializer
from .models import BlogCategory,BlogPost,BlogComment

def home(request) :
    return HttpResponse("<h1>Hello, Welcome to Homepage</h1>")

from rest_framework.viewsets import ModelViewSet
class BlogCategoryMVS(ModelViewSet) :
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogPostMVS(ModelViewSet) :
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogCommentMVS(ModelViewSet) :
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer