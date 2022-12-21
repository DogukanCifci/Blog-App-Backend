from django.urls import path,include
from .views import home, BlogCategoryMVS


from rest_framework import routers
router = routers.DefaultRouter()
router.register('blogcategorymvs', BlogCategoryMVS)

urlpatterns = [
    path('', home),
   # path('category_list/', BlogCategoryMVS.as_view())
   path('', include(router.urls))
]