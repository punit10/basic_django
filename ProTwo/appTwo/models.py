from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=264)
    email = models.CharField(max_length=264)
    confirm_email = models.CharField(max_length=264)
    address = models.CharField(max_length=264)


    def __str__(self) -> str:
        return self.user_fname
    