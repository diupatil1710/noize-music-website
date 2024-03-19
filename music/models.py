from django.db import models
import os
# class registration(models.Model):
#     first_name=models.CharField(max_length=200)
#     last_name=models.CharField(max_length=200)
#     email=models.EmailField('@',max_length=255)
#     password=models.CharField(null=True,max_length=15)
#     def __str__(self):
#         return self.useremail

class category(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to="image",null=True)
    def __str__(self):
        return self.name
    
class user_login(models.Model):
    photo=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=200)
    email=models.EmailField(("@"), max_length=254)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    song_title= models.CharField(max_length=250)
    image = models.ImageField(upload_to="images")
    song = models.FileField(upload_to="images")

    def __str__(self):
        return self.name

class contact(models.Model):
    userid= models.AutoField(primary_key=True)
    username=models.CharField(max_length=40)
    phone=models.CharField(max_length=10)
    email=models.EmailField(('@'),max_length=256)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)

    def __str__(self):
        return self.firstname
