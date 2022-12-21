from rest_framework import serializers
from .models import BlogCategory,BlogPost,BlogComment


class BlogCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogCategory
        # fields = "__all__"
        fields = [
            "id",
            "author",
            "name",
            "created_date",
            "updated_date",
        ]

   
class BlogPostSerializer(serializers.ModelSerializer) :

    class Meta :
        model = BlogPost

        fields = [
            "id",
            "title",
            "content",
            "image",
            "created_date",
            "updated_date",
            "category",
            "user",
        ]
    
class BlogCommentSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = BlogComment

        fields = [
            "id",
            "first_name",
            "last_name",
            "title",
            "comment",
            "created_date",
            "updated_date",
            "post",
            "user",
        ]