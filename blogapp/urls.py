from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('blogcategoryview', BlogCategoryView)
router.register('blogpostview', BlogPostView)
router.register('blogcommentview', BlogCommentView)

urlpatterns = [
    path('', home),
    path('', include(router.urls))
]