from rest_framework import serializers
from .models import BlogCategory,BlogPost,BlogComment

#------------------------ FixSerializer ----------------------------#
class FixSerializer(serializers.ModelSerializer) :
    pass

    class Meta :
        #Normalde bu exclude hepsinde tanimlayacaktim. Ama hepsinde ayni sekilde olacagi icin bu FixSerializer'da bir kere tanimlayip hepsine atadim. Atamayi da her bir serializer () icine kendi olusturdugum FixSerializer classini yazdim.
        exclude = [
            'created_date',
            'updated_date'
        ]
#------------------------ Serializers ----------------------------#

class BlogCategorySerializer(FixSerializer):
    
    class Meta(FixSerializer.Meta):
        model = BlogCategory
        # fields = "__all__" #-->1. Metod

        #2.Metod
        """ fields = [ 
            "id",
            "author",
            "name",
        ] """

        #3.METOD --> exclude Hepsini cagir ama exclude icine yazdiklarim haricindeki anlamina gelir
        """ exclude = [
            'created_date',
            'updated_date'
        ]
    """

class BlogPostSerializer(FixSerializer) :

    class Meta(FixSerializer.Meta) :
        model = BlogPost

  
    
class BlogCommentSerializer(serializers.ModelSerializer) :
    
    class Meta(FixSerializer.Meta) :
        model = BlogComment

      