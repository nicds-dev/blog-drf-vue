# Generated by Django 5.0.2 on 2024-04-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_user_comment_author_rename_user_like_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
