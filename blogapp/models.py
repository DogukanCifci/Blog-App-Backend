from django.db import models
from django.contrib.auth.models import User

#-------------------------- Fix Models --------------------------#
class FixModels(models.Model) :
    user = models.ForeignKey(User,verbose_name="Kullanici", on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name="Olusturulma Tarihi",auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Güncellenme Tarihi",auto_now=True)

    class Meta :
        abstract = True ## DB'de bu tabloyu olusturmasin diye bu komutu yazdik.

#-------------------------- Models --------------------------#
#!!!!! Kendi olusturdugum FixModels zaten models.Model oldugu icin alttaki classlarda bir daha extra olarak models.Model yazmama gerek yok. Knedi olusturdugumuz FixModels'ten onu alir.
class BlogCategory(FixModels) :
    name = models.CharField(verbose_name="Kategori Adi",max_length=64)   

    def __str__(self):
        return self.name


class BlogPost(FixModels) :
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    content = models.TextField()
    viewed = models.IntegerField(default=0)
    
    def __str__(self) :
        return f"{self.title} | {self.user}"


class BlogComment(FixModels) :
    blog_post = models.ForeignKey(BlogPost, verbose_name="Blog Yazisi",on_delete=models.CASCADE)
    first_name =models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.title}"


