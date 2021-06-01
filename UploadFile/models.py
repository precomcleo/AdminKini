import os
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

'''
Photo：照片模型
'''
class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)

# 刪除時連同刪除照片
@receiver(pre_delete, sender=Photo)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)

'''
File：檔案模型
'''
class File(models.Model):
    name = models.CharField(primary_key=True, max_length=50)    #檔名稱
    path = models.CharField(max_length=100)                     #檔案儲存路徑
    upload_date = models.DateTimeField(default=timezone.now)    #上傳時間

# 刪除時連同刪除文件
@receiver(pre_delete, sender=File)
def delete_upload_files(sender, instance, **kwargs):
    files = getattr(instance, 'path', '')
    if not files:
        return 
    if os.path.isfile(files):
        os.remove(files)