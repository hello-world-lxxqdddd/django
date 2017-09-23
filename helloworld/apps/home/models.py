#_*_coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HomePage(models.Model):
    banner_1= models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",verbose_name=u'轮播图1')
    banner_2= models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",verbose_name=u'轮播图2')
    banner_3= models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",verbose_name=u'轮播图3')
    welcome_title = models.CharField(max_length=100,verbose_name=u"欢迎标题")
    welcome_text1 = models.CharField(max_length=100, verbose_name=u"欢迎诗1")
    welcome_text2 = models.CharField(max_length=100, verbose_name=u"欢迎诗2")
    welcome_text3 = models.CharField(max_length=100, verbose_name=u"欢迎诗3")

    class Meta:
        verbose_name = u"首页"
        verbose_name_plural = verbose_name

class UserProfile(models.Model):
    name = models.CharField(max_length=12,verbose_name=u'名字')
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",verbose_name=u'头像')
    introduce_title = models.CharField(max_length=100,verbose_name=u'个人标题简介')
    motto = models.CharField(max_length=50,verbose_name=u'格言')
    introduce_p1 = models.TextField(verbose_name=u'个人简介第一段')
    introduce_p2 = models.TextField(verbose_name=u'个人简介第二段')
    introduce_p3 = models.TextField(verbose_name=u'个人简介第三段')


    class Meta:
        verbose_name=u'个人简介'
        verbose_name_plural=verbose_name