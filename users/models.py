from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	bio = models.TextField(max_length=500, null=True, blank=True)
	url = models.CharField(max_length=500,null=True, blank=True)

class Picture(models.Model):
    File = models.FileField(null=True, blank=True)
