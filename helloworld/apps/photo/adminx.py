#_*_coding:utf-8

from .models import Photo
import xadmin

class PhotoAdmin(object):
    list_display = ['img','title','content','create_data']
    search_fields = ['title','content','create_data']
    list_filter = ['img','title','content','create_data']


xadmin.site.register(Photo,PhotoAdmin)