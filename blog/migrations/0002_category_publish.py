# Generated by Django 4.0.3 on 2022-03-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='publish',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
