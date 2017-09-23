#_*_coding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Blog(models.Model):
    blog_image = models.ImageField(upload_to="image/%Y/%m",verbose_name=u'文章配图',default="image/default_article.png",max_length=100)
    title = models.CharField(max_length=50,verbose_name=u"文章标题")
    content = models.TextField(verbose_name=u"文章简介")
    detail =models.TextField(verbose_name=u"文章内容")
    tag1 = models.CharField(max_length=10,verbose_name=u"标签1",default=u"生活")
    tag2 = models.CharField(max_length=10,verbose_name=u"标签2",default=u"随笔")
    tag3 = models.CharField(max_length=10,verbose_name=u"标签3",default=u"操蛋")
    tag4 = models.CharField(max_length=10,verbose_name=u"标签4",default=u"玩意儿")
    click_num = models.IntegerField(verbose_name=u"点击数",default=0)
    creat_data = models.DateField(default=datetime.now,verbose_name=u'创建日期')

    class Meta:
        verbose_name = u"博客管理"
        verbose_name_plural=verbose_name