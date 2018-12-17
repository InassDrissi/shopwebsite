from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'mall'
urlpatterns = [
    # /music
    path('', views.index, name="index"),
    path('<int:shop_id>/', views.detail, name="detail"),

]