from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from .views import logout, UserView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserView)

urlpatterns = [
    #!!!Settings.py 'de rest_framework.authtoken eklemeyi unutma INSTALLED_APP Kismina. Login'de token elde etmek icin
    path('login/', obtain_auth_token), #Otomatik token olusturulmasi icin Postman'de Headers kismindaki authorization kapali olmali. Ama logout olacagimiz zaman token silinecegi icin authorization ve karsisindaki Token ... acik olmali
    path('logout/', logout),
    path('',include(router.urls)),
]

