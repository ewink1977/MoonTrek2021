# Generated by Django 3.2.3 on 2021-05-20 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MoonTrekStories', '0006_comment_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='moontrekchapters',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moontrekchapters',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='moontrekstories',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moontrekstories',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]