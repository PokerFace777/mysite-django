# Generated by Django 4.0.3 on 2022-03-15 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_content_comment_comment_remove_comment_upvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=100000),
        ),
    ]
