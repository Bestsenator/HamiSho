# Generated by Django 4.2 on 2023-11-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_candidate_sirname'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Version', models.CharField(default='1.0.0', max_length=50)),
            ],
        ),
    ]
