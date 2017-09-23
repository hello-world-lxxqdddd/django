#_*_coding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Photo(models.Model):
    img = models.ImageField(upload_to="image/%Y/%m",max_length=200,default='image/default.png')
    title = models.CharField(max_length=50,verbose_name=u'标题')
    content = models.CharField(max_length=50,verbose_name=u"内容简介")
    create_data = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = u"照片"
        verbose_name_plural = verbose_name