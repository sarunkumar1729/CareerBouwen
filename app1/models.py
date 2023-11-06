from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    profile_user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='profile_photos/', blank=True)
    email=models.EmailField(null=True)
    phone1=models.CharField(max_length=255,null=True)
    phone2=models.CharField(max_length=255,null=True)
    current_address=models.CharField(max_length=255)
    permanant_address=models.CharField(max_length=255)
    Education=models.CharField(max_length=255)
    skills=models.CharField(max_length=255)
    certifications=models.CharField(max_length=255)
    resume=models.FileField(upload_to='resume/',blank=True)
    class Meta:
        app_label='app1'
