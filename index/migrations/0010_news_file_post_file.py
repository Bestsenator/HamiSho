# Generated by Django 5.0.1 on 2024-02-21 05:18

import index.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_delete_infoapp_candidate_appfile_candidate_appname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to=index.models.uploadToPost),
        ),
        migrations.AddField(
            model_name='post',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to=index.models.uploadToPost),
        ),
    ]
