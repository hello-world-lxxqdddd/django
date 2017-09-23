#_*_coding:utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProfileAbout(models.Model):
    name = models.CharField(max_length=10,verbose_name=u"名字")
    birthday = models.CharField(max_length=20,verbose_name=u'生日')
    email = models.CharField(max_length=50,verbose_name=u"邮箱")
    phone = models.CharField(max_length=11,verbose_name=u"手机号码")
    adress = models.CharField(max_length=50,verbose_name=u'地址')
    good_at1 = models.CharField(max_length=50,verbose_name=u"特长1")
    good_at2 = models.CharField(max_length=50,verbose_name=u"特长2")
    good_at3 = models.CharField(max_length=50,verbose_name=u"特长3")
    poem_title = models.CharField(max_length=20,verbose_name=u"诗歌题目")
    poem_content1 = models.CharField(max_length=50,verbose_name=u"诗句1")
    poem_content2 = models.CharField(max_length=50,verbose_name=u"诗句2")
    poem_content3 = models.CharField(max_length=50,verbose_name=u"诗句3")
    poem_content4 = models.CharField(max_length=50,verbose_name=u"诗句4")
    poem_content5 = models.CharField(max_length=50,verbose_name=u"诗句5")
    poem_content6 = models.CharField(max_length=50,verbose_name=u"诗句6")
    poem_content7 = models.CharField(max_length=50,verbose_name=u"诗句7")
    poem_content8 = models.CharField(max_length=50,verbose_name=u"诗句8")
    poem_content9 = models.CharField(max_length=50,verbose_name=u"诗句9")
    poem_content10 = models.CharField(max_length=50,verbose_name=u"诗句10")
    poem_content11= models.CharField(max_length=50,verbose_name=u"诗句11")

    class Meta:
        verbose_name = u"个人简介"
        verbose_name_plural = verbose_name
