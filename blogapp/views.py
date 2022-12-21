
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import BlogCategorySerializer
from .models import BlogCategory

def home(request) :
    Response({
        "message" : "That works!"
    })

# from rest_framework.views import APIView

# class BlogCategoryCreate(APIView) :
#     def get(self,request) :
#         blog_category = BlogCategory.objects.all()
#         serializer = BlogCategorySerializer(blog_category, many = True)
#         return Response(serializer.data)


from rest_framework.viewsets import ModelViewSet
class BlogCategoryMVS(ModelViewSet) :
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
