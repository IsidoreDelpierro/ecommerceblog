from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime import datetime, date

# Create your models here. 

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

 
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)#, default="eCommerce Blog")
    meta_tag = models.CharField(max_length=255, default="kaavi")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField() 
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="Scooter")

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title + ' | ' + str(self.author)  

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
        #return reverse('home')