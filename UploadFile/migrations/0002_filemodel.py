# Generated by Django 2.2.7 on 2021-05-31 21:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=100)),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
