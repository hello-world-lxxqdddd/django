#_*_coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=10,verbose_name=u"你的名字")
    email = models.CharField(max_length=30,verbose_name=u"邮箱")
    phone = models.CharField(max_length=11,verbose_name=u"手机号码")
    adress = models.CharField(max_length=100,verbose_name=u"地址")
    website = models.CharField(max_length=100,verbose_name=u"网址")
    what_do_you_want = models.CharField(max_length=30,verbose_name=u"约什么？")
    content = models.TextField(verbose_name=u"具体消息")

    class Meta:
        verbose_name = u"联系我"
        verbose_name_plural = verbose_name