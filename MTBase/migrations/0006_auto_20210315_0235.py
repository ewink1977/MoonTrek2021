# Generated by Django 3.1.7 on 2021-03-15 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MTBase', '0005_auto_20210315_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
