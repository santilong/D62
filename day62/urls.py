"""day62 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index.html', views.index),
    url('ajax1.html', views.ajax1),
    url('upload.html', views.upload),
    url('uploaded', views.uploaded),
    url('jsonp.html', views.jsonp),
    url('jsonpcommit.html', views.jsonpcommit),
    url('bxslider.html', views.bxslider),
    url('zan.html', views.zan),
    url('article-(?P<article_type_id>\d+)-(?P<category_id>\d+).html', views.article,name='article'),
    url('picwall.html', views.picwall),
    url('getdata.html', views.getdata),

]
