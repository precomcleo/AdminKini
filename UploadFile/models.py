from django.db import models
from django.utils import timezone

class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)

# 檔案模型
class File(models.Model):
    # 檔名稱
    name = models.CharField(max_length=50)
    # 檔案儲存路徑
    path = models.CharField(max_length=100)
    # 上傳時間
    upload_time = models.DateTimeField(default=timezone.now)