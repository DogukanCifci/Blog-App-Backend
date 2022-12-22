from rest_framework import serializers
from .models import BlogCategory,BlogPost,BlogComment

#------------------------ FixSerializer ----------------------------#
class FixSerializer(serializers.ModelSerializer) :
    #Burda yazmamin sebebi bütün serializerlarda da ayni sekilde olmasini istedigim icin. FixSerializer olusturmasam hepsinin icinde tek tek yazmam gerekir.
    user_id=serializers.IntegerField(read_only=True)
    user = serializers.StringRelatedField() # Hangi Kullanici oldugunu göstermesi icin. Bunu yaomazsam user karsisina olsuturma sirasina göre, 1,2,3.. vb yazar.

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
    #Bunlar önemli. API'de görüntülerken farki görebilirim. SIlip bir daha görünümünü kontrol et tekrar baktiginda
    blog_category_id = serializers.IntegerField()
    blog_category = serializers.StringRelatedField()
    
    class Meta(FixSerializer.Meta) :
        model = BlogPost

  
    
class BlogCommentSerializer(serializers.ModelSerializer) :
    blog_post_id = serializers.IntegerField()
    blog_post = serializers.StringRelatedField()

    class Meta(FixSerializer.Meta) :
        model = BlogComment

      