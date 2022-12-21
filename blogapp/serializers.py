from rest_framework import serializers
from .models import BlogCategory


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

   