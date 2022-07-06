from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    followers=models.ManyToManyField(User,blank=True,related_name="followers")
    followings=models.ManyToManyField(User,blank=True,related_name="followings")
    profile_picture=models.ImageField( upload_to='profilepics')

class post(models.Model):
    user=models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    image= models.ImageField(null=True)
    Likes=models.ManyToManyField(User,blank=True,related_name="likes")
    profile=models.ForeignKey(Profile,null=True,related_name="profile",on_delete=models.CASCADE)

class reels(models.Model):
    reels=models.FileField(null=True)
    likes=models.ManyToManyField(User,blank=True)

class story(models.Model):
    Story=models.ImageField(null=True)
    profile=models.ForeignKey(Profile,null=True,on_delete=models.DO_NOTHING)