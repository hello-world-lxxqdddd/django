from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import Photo

# Create your views here.
class PhotoView(View):
    def get(self,request):
        photoes = Photo.objects.all()

        return render(request,"shop.html",{"photoes":photoes})


class PhotoDetailView(View):
    def get(self,request,imgs_id):
        photo = Photo.objects.get(id=int(imgs_id))
        return render(request,'card-hipotama.html',{'photo':photo})
        pass
