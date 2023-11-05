from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    profile_user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='profile_photos/')
    email=models.EmailField()
    phone1=models.CharField()
    phone2=models.CharField()
    current_address=models.CharField(max_length=255)
    permanant_address=models.CharField(max_length=255)
    Education=models.CharField(max_length=255)
    skills=models.CharField(max_length=255)
    certifications=models.CharField(max_length=255)

