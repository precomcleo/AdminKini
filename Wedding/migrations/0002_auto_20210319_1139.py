# Generated by Django 3.1.6 on 2021-03-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wedding', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'ordering': ('-object_id',), 'verbose_name_plural': '用户留言信息'},
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='主键'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='用户名'),
        ),
        migrations.AlterModelTable(
            name='usermessage',
            table='user_message',
        ),
    ]