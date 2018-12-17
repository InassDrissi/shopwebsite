
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('mall/', include('mall.urls')),

]