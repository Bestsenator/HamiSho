# Generated by Django 4.2 on 2023-10-30 13:16

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIKEY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApiKey', models.TextField(default=index.models.sesProduction)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='Candidate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nSupport',
        ),
        migrations.AddField(
            model_name='candidate',
            name='Cv',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='candidate',
            name='Sound',
            field=models.FileField(default='', upload_to=index.models.uploadToSound),
        ),
        migrations.AddField(
            model_name='user',
            name='Code',
            field=models.IntegerField(default=index.models.ranInt, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='user',
            name='RegisterTime',
            field=django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime),
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.candidate')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.user')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to=index.models.uploadToPost)),
                ('Caption', models.TextField(max_length=2000)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Image', models.ImageField(upload_to=index.models.uploadToNews)),
                ('Content', models.TextField(max_length=2000)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='MessageToCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Family', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone', models.CharField(blank=True, max_length=11, null=True)),
                ('Address', models.TextField(blank=True, max_length=500, null=True)),
                ('Message', models.TextField(default='', max_length=2000)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
                ('User', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='index.user')),
            ],
        ),
    ]