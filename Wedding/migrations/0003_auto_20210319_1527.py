# Generated by Django 3.1.6 on 2021-03-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wedding', '0002_auto_20210319_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'ordering': ('-object_id',), 'verbose_name_plural': '用户留言訊息'},
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='address',
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='信箱'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.CharField(max_length=100, verbose_name='留言訊息'),
        ),
    ]
