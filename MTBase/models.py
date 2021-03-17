from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
        )
    image = models.ImageField(
        default = 'default.png',
        upload_to = 'profilepics'
    )
    about = HTMLField()

    def __str__(self):
        return f'{self.user.username} Profile'

