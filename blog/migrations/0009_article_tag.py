# Generated by Django 3.2 on 2022-07-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='articles', to='blog.Tag'),
        ),
    ]