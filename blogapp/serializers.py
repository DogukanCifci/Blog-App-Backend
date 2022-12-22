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
class BlogCommentSerializer(serializers.ModelSerializer) :
    blog_post_id = serializers.IntegerField()
    blog_post = serializers.StringRelatedField()

    class Meta(FixSerializer.Meta) :
        model = BlogComment


class BlogPostSerializer(FixSerializer) :
    #Bunlar önemli. API'de görüntülerken farki görebilirim. SIlip bir daha görünümünü kontrol et tekrar baktiginda
    blog_category_id = serializers.IntegerField()
    blog_category = serializers.StringRelatedField()
    blog_comments = BlogCommentSerializer(read_only=True, many = True) #Amacim sadece görüntülemek oldugu icin read_only=True yazdim. Yoksa kaydedilmesi gerekn bir sey olarak görür db onu
    class Meta(FixSerializer.Meta) :
        model = BlogPost

  
    
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


      

#!!!!!!! related_name models'de alt tabloya serializers'ta üst tabloya yazilir. Isim iki yerde de ayni olmali !!!!!!!!

#RELATED_NAME KULLANMAMIN SEBEBI, POSTLARI DB GÖRÜNTÜLERKEN O POST ICIN YAPILAN COMMENTLERIN'DE GÖZÜKMESI ICIN. Iliskili oldugundan dolayi bu kullanimi yaparak bunu saglayabiliriz.. blogapp/blogpostviews/ urle gidip mantigi görüp anlayabilirim

#!!!!!!Models.py'dan farkli olarak burada child en üste yazilir parent en alta yazilir. Cünkü Related iliskisi kullanmam gerekirse ve parent en yukarda olursa, realted ilsikisinde parent serializer icinde child serializer cagirmam gerekecegi icin ve yazilim dilleri kodlari yukardan asagiya dogru okudugu icin parent icinde child undefined olarak gözükür. Anlamadiysan Blog_Post_Serializers ile Blog_Comments_Serializer yerini degistirip görebilirim