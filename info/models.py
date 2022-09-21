from django.db import models
from django.urls import reverse

# Create your models here.

class BusinessInfo(models.Model):
    name = models.CharField(max_length=200, default="Name of Business") 
    subname = models.CharField(max_length=200, default="Your Slogan")
    about = models.CharField(max_length=500, default="About the Business")
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    slogan = models.CharField(max_length=200, default="Slogan")
    logo = models.ImageField(upload_to="images/logo/")
    website_url = models.CharField(max_length=255, default="#")
    facebook_url = models.CharField(max_length=255, default="https://www.facebook.com/")
    twitter_url = models.CharField(max_length=255, default="https://www.twitter.com/")
    instagram_url = models.CharField(max_length=255, default="https://www.instagram.com/")
    pinterest_url = models.CharField(max_length=255, default="https://www.pinterest.com/")
    tiktok_url = models.CharField(max_length=255, default="https://www.tiktok.com/")
    youtube_url = models.CharField(max_length=255, default="https://www.youtube.com/")
    blogger_url = models.CharField(max_length=255, default="https://www.blogger.com/")
    
    class Meta:
    	verbose_name_plural = "Business Info"

    @property 
    def logoURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url
    
    def __str__(self):
    	return str(self.name)

    def get_absolute_url(self):
    	return reverse('home') 
        
        
