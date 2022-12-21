from django.urls import path,include
from .views import home, BlogCategoryMVS,BlogPostMVS,BlogCommentMVS


from rest_framework import routers
router = routers.DefaultRouter()
router.register('blogcategorymvs', BlogCategoryMVS)
router.register('blogpostmvs', BlogPostMVS)
router.register('blogcommentmvs', BlogCommentMVS)
urlpatterns = [
    path('', home),
    path('', include(router.urls))
]