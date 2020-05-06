from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstaViewSet, InstaListView

app_name = 'projectmini'

urlpatterns = [
    path('',InstaListView.as_view(), name='insta_feed'),

]

"""
router = DefaultRouter()
router.register('posts', InstaViewSet, basename='posts')


custom_urlpatterns = [
    url(r'categories/(?P<category_pk>\d+)/recipes$', CategoryRecipes.as_view(), name='category_recipes'),
    url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$', SingleCategoryRecipe.as_view(), name='single_category_recipe'),
    url(r'public-recipes/', PublicRecipes.as_view(), name='public-recipes'),
    url(r'public-recipes/(?P<pk>\d+)/$', PublicRecipesDetail.as_view(), name='public-recipes-detail')
]
"""

# urlpatterns = router.urls
# urlpatterns += custom_urlpatterns