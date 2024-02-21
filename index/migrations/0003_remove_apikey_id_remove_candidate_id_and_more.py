# Generated by Django 4.2 on 2023-10-30 13:18

from django.db import migrations, models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_apikey_remove_user_candidate_remove_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apikey',
            name='id',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='id',
        ),
        migrations.RemoveField(
            model_name='messagetocandidate',
            name='id',
        ),
        migrations.RemoveField(
            model_name='news',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.RemoveField(
            model_name='supporter',
            name='id',
        ),
        migrations.AddField(
            model_name='apikey',
            name='Code',
            field=models.IntegerField(default=index.models.ranInt, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='candidate',
            name='Code',
            field=models.IntegerField(default=index.models.ranInt, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='messagetocandidate',
            name='Code',
            field=models.IntegerField(default=index.models.ranInt, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='news',
            name='Code',
            field=models.IntegerField(default=index.models.ranInt, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='post',
            name='Code',
            field=models.IntegerField(default=index.models.ranInt, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='supporter',
            name='Code',
            field=models.IntegerField(default=index.models.ranInt, primary_key=True, serialize=False),
        ),
    ]
