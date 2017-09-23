"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from home.views import IndexView
from django.views.static import serve
from helloworld.settings import MEDIA_ROOT
from profile_about.views import ProfileView
from photo.views import PhotoView,PhotoDetailView
from blog.views import BlogView,BlogDetailView
from contact.views import ContactView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$',IndexView.as_view(),name="index"),
    url('^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url('^about/$',ProfileView.as_view(),name='about'),
    url('^photo/$',PhotoView.as_view(),name='photo'),
    url('^blog/$',BlogView.as_view(),name='blog'),
    url('^contact/$',ContactView.as_view(),name='contact'),
    url('^photo/(?P<imgs_id>\d+)$',PhotoDetailView.as_view(),name='projects'),
    url('^blog/(?P<blog_id>\d+)/(?P<user_id>\d+)$', BlogDetailView.as_view(), name='blog_detail'),

]
