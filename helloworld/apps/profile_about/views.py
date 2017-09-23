#_*_coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from .models import ProfileAbout
from home.models import UserProfile
# Create your views here.
class ProfileView(View):
    def get(self,request):
        profile_abouts =UserProfile .objects.all()
        for i in profile_abouts:
            profile_about = i
        return render(request,"about.html",{"profile_about1":profile_about})