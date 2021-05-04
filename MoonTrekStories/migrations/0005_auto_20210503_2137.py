# Generated by Django 3.2 on 2021-05-04 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoonTrekStories', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='moontrekstories',
            name='fullStoryEPUB',
            field=models.FileField(null=True, upload_to='full_stories/EPUB/'),
        ),
        migrations.AddField(
            model_name='moontrekstories',
            name='fullStoryPDF',
            field=models.FileField(null=True, upload_to='full_stories/PDF/'),
        ),
    ]
