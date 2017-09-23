#_*_coding:utf-8

from .models import Blog
import xadmin

class BlogAdmin(object):
    list_display = ['blog_image','title','content','detail','tag1','tag2','tag3','tag4','click_num','creat_data']
    search_fields = ['blog_image','title','content','detail','tag1','tag2','tag3','tag4','click_num']

    list_filter = ['blog_image','title','content','detail','tag1','tag2','tag3','tag4','click_num','creat_data']



xadmin.site.register(Blog,BlogAdmin)