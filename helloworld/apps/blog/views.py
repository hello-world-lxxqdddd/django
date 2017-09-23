from django.shortcuts import render
from django.views.generic.base import View
from .models import Blog
from home.models import UserProfile

# Create your views here.
class BlogView(View):
    def get(self,request):
        blogs = Blog.objects.all()

        return render(request,"blog.html",{"blogs":blogs})


class BlogDetailView(View):
    def get(self,request,blog_id,user_id):
        blog = Blog.objects.get(id=int(blog_id))
        user = UserProfile.objects.get(id=int(user_id))
        return render(request,'single.html',{'blog':blog,'user':user})
        pass