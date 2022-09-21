class ProfileListView(ListView):
    template_name = "index.html"
    paginate_by = 3 
    queryset = Profile.objects.all()


    

class Corporate(models.Model):
    name = models.CharField(max_length=200, default="Name of Business")
    description = models.CharField(max_length=255, default="About the Business")
    slogan = models.CharField(max_length=200, default="Slogan")
    logo = models.ImageField(upload_to="images/logo/")
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    website_url = models.CharField(max_length=255, default="#")
    facebook_url = models.CharField(max_length=255, default="https://www.facebook.com/")
    twitter_url = models.CharField(max_length=255, default="https://www.twitter.com/")
    instagram_url = models.CharField(max_length=255, default="https://www.instagram.com/")
    pinterest_url = models.CharField(max_length=255, default="https://www.pinterest.com/")
    tiktok_url = models.CharField(max_length=255, default="https://www.tiktok.com/")
    youtube_url = models.CharField(max_length=255, default="https://www.youtube.com/")
    blogger_url = models.CharField(max_length=255, default="#")

    class Meta:
        verbose_name_plural = "Business Info"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')