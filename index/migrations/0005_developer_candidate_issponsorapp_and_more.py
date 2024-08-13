# Generated by Django 4.2 on 2023-11-03 10:29

import django.contrib.postgres.fields
from django.db import migrations, models
import django_jalali.db.models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_apikey_code_alter_candidate_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('Code', models.IntegerField(default=index.models.ranInt, primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=150)),
                ('Expertise', models.CharField(default='', max_length=150)),
                ('Image', models.ImageField(upload_to=index.models.uploadToDeveloper)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='isSponsorApp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='Color',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=16), default=list, help_text='1.Background - 2.Buttons - 3.SloganColor', size=None),
        ),
    ]