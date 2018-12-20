from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'mall'
urlpatterns = [
    # /music
    path('', views.index, name="index"),
    path('<int:shop_id>/', views.detail, name="detail"),
    path('<shop_id>/favorite/', views.favorite, name='favorite'),
    path('<shop_id>/nofavorite/', views.nofavorite, name='nofavorite'),
    path('preferred/', views.preferred, name='preferred'),

]