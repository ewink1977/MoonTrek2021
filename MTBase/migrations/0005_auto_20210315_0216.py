# Generated by Django 3.1.7 on 2021-03-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MTBase', '0004_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.TextField(max_length=200),
        ),
    ]