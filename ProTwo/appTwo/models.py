from django.db import models

# Create your models here.

class Users(models.Model):
    user_fname = models.CharField(max_length=264)
    user_lname = models.CharField(max_length=264)
    user_email = models.CharField(max_length=264)

    def __str__(self) -> str:
        return self.user_fname
    