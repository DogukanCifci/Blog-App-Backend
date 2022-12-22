
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogCategorySerializer,BlogPostSerializer,BlogCommentSerializer
from .models import BlogCategory,BlogPost,BlogComment
from rest_framework.viewsets import ModelViewSet

def home(request) :
    return HttpResponse("<h1>Hello, Welcome to Homepage</h1>")

class BlogCategoryView(ModelViewSet) :
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogPostView(ModelViewSet) :
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    #Override yaparak her görüntülemede viewd sayisini 1 artirmaya caisacagiz.
 #Metodun aynisini aldik super() ile orijinal halini bozmadan calistircam ve Üstüne eklemeler yapicam.
    def retrieve(self, request, *args, **kwargs) :

        #------Buradan --->
        instance = self.get_object() # ---> Bu komutla blogpost'daki argslari aldik. Yani keywordleri.Print(instance) ile blogposttaki keywordleri görebilirim. Benim isim sadece viewed ile oldugu icin instance.viewed demem yeterli
        instance.viewed += 1
        instance.save()
        #------>Buraya kadar benim eklemek istedigim kodlar
        #Geri kalan ise o metodun icinden kopyala yapistir yaptigim kod. Override etmek icin. Bu mantigi her yerde kullanabilirim. Gidip override etmek istedigim metoda giderim. O fonksiyonu kopyalarim. Benim yazdigim kisim disindakiler gibi yani.(return ve def fonksiyonu)
        
        return super().retrieve(self, request, *args, **kwargs) #Orijinal methodu bozmadan calistirmam icin bunu kullandim. Gidip metodun icinden kopayala yapistir yaptik

class BlogCommentView(ModelViewSet) :
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer