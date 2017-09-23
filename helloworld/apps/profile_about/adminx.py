#_*_coding:utf-8

from .models import ProfileAbout
import xadmin

class ProfileAboutAdmin(object):
    list_display = ['name','birthday','email','phone','adress','good_at1','good_at2','good_at3','poem_title','poem_content1','poem_content2','poem_content3','poem_content4','poem_content5','poem_content6','poem_content7','poem_content8','poem_content9','poem_content10','poem_content11']
    search_fields = ['name','birthday','email','phone','adress','good_at1','good_at2','good_at3','poem_title','poem_content1','poem_content2','poem_content3','poem_content4','poem_content5','poem_content6','poem_content7','poem_content8','poem_content9','poem_content10','poem_content11']
    list_filter = ['name','birthday','email','phone','adress','good_at1','good_at2','good_at3','poem_title','poem_content1','poem_content2','poem_content3','poem_content4','poem_content5','poem_content6','poem_content7','poem_content8','poem_content9','poem_content10','poem_content11']


xadmin.site.register(ProfileAbout,ProfileAboutAdmin)