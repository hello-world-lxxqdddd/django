#_*_coding:utf-8

from .models import Contact
import xadmin

class ContactAdmin(object):
    list_display = ['name','email','adress','website','what_do_you_want','content']
    search_fields = ['name','email','adress','website','what_do_you_want','content']
    list_filter = ['name','email','adress','website','what_do_you_want','content']



xadmin.site.register(Contact,ContactAdmin)