from django.db import models
from django.urls import reverse
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
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def get_absolute_url(self):
        return reverse('base:profilePage', kwargs={'user': self.user})

