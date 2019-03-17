from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.models import UserProfile
from django.contrib.auth.models import User

class Autopost(models.Model):
    id=models.IntegerField(primary_key=True, auto_created=True)
    title=models.CharField(max_length=200,default=None)
    posturl = models.CharField(max_length=200,default=None)
    selection =models.CharField(max_length=100,default=None)
    gettag = models.CharField(max_length=100,default=None)
    def __str__(self):
        return self.posturl

    def get_absolute_url(self):
        return reverse('autopost:autopost-detail', kwargs={
            'id': self.id
        })
    
    def get_update_url(self):
        return reverse('autopost:autopost-update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('autopost:autopost-delete', kwargs={
            'id': self.id
        })