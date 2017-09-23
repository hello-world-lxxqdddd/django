#_*_coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from .models import HomePage,UserProfile
from photo.models import Photo
from blog.models import Blog
# Create your views here.

class IndexView(View):
    def get(self,request):
        home_page_blogs = Blog.objects.all()
        home_pages = HomePage.objects.all()
        home_page_users = UserProfile.objects.all()
        home_page_photos = Photo.objects.all()
        home_page_photo = home_page_photos.order_by("create_data")[:6]
        home_page_blog = home_page_blogs.order_by("creat_data")[:12]
        new_blog=home_page_blogs.order_by('creat_data')[0]
        for i in home_pages:
            home_page = i
        for home_page_user in home_page_users:
            home_page_user = home_page_user
        return render(request,'index.html',{"homepage":home_page,"home_page_photo":home_page_photo,"home_page_blog":home_page_blog,"home_page_user":home_page_user,'new_blog':new_blog})

