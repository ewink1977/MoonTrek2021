# Generated by Django 3.2.7 on 2021-09-02 23:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('MTBase', '0008_landingalert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingalert',
            name='alertText',
            field=tinymce.models.HTMLField(max_length=350),
        ),
    ]
