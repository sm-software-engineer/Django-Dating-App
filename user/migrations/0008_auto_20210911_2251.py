# Generated by Django 3.1.5 on 2021-09-11 22:51

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210910_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphoto',
            name='file_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userphoto',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.content_file_name),
        ),
    ]
