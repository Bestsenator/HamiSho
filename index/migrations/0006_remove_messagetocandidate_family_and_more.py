# Generated by Django 4.2 on 2023-11-03 11:02

from django.db import migrations, models
import django.db.models.deletion
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_developer_candidate_issponsorapp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagetocandidate',
            name='Family',
        ),
        migrations.AddField(
            model_name='candidate',
            name='SeriesDeveloper',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='developer',
            name='SeriesDeveloper',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('Code', models.IntegerField(default=index.models.ranInt, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Logo', models.ImageField(upload_to=0)),
                ('Slogan', models.CharField(max_length=150)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.candidate')),
            ],
        ),
    ]
