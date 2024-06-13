"""
URL configuration for yugabyteTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, re_path, path
from rest_framework import routers
from testdb.views import UserViewSet, home, add_movie, upload_success
from django.contrib import admin

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'movie', UserViewSet)
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    path('add_movie/', add_movie),
    path('upload_success', upload_success),
]

