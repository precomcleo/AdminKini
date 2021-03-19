#coding: utf-8
from django.db import models
import django.utils.timezone as timezone

class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, primary_key=True, verbose_name='主键', default='')
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'信箱')
    message = models.CharField(max_length=100, verbose_name=u'留言訊息')
    createtime = models.DateTimeField('保存日期',default = timezone.now)

    class Meta:
        db_table = 'user_message'
        ordering = ('-object_id',)
        verbose_name_plural = u'用户留言訊息'
