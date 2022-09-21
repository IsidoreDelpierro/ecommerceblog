from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from members.models import Profile as Customer
#from . import utils #This was the problematic line. Please don't uncomment it. It was the circular import that made everything else fall apart. 
from ckeditor.fields import RichTextField

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, null=True, blank=True, default="Describe this collection")
    image = models.ImageField(null=True, blank=True, upload_to="images/collections/")

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse('home')


#https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
class DecimalRangeField(models.DecimalField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value 
        models.DecimalField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value':self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(DecimalRangeField, self).formfield(**defaults)


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    subname = models.CharField(max_length=200, null=True, default="Subname")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=250, null=True, default="Snippet")
    digital = models.BooleanField(default=False, null=True, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True, default="images/default/default_product.png", upload_to="images/products/")
    #rating = models.DecimalField(max_digits=1, decimal_places=1, default=3.8, null=True)
    rating_manual = DecimalRangeField(min_value=0.0, max_value=5.0, max_digits=2, decimal_places=1, default=4.3)
    likes = models.ManyToManyField(User, related_name='products')

    def total_likes(self):
        return self.likes.count()

    def total_versions(self):
        return self.versions.count()

    @property 
    def rating(self):
        product_reviews = self.review_set.all() 
        sum_of_ratings = 0
        for review in product_reviews:
            sum_of_ratings += review.rating 
        if product_reviews.count() <= 0:
            average_rating = self.rating_manual 
        else: 
            average_rating = sum_of_ratings / product_reviews.count() 
            print("Rating for {} is {}".format(self.name, average_rating))
        return average_rating 

    def count_reviews(self):
        all_reviews_for_this_product = self.review_set.all() 
        number_of_reviews = all_reviews_for_this_product.count()
        if number_of_reviews <= 1:
            number_of_reviews = 1 
        else:
            pass
        return number_of_reviews

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Version(models.Model):
    name = models.CharField(max_length=200, null=True) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/products/versions")

    class Meta:
        verbose_name_plural = "Product Versions"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        version = str(self.product.name)+" | "+str(self.name)
        return version


class Review(models.Model):
    rating = DecimalRangeField(min_value=0.0, max_value=5.0, max_digits=2, decimal_places=1, default=4.3)
    review = models.CharField(max_length=200, null=True) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return str(self.customer) + " on " + str(self.product)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderItems = self.orderitem_set.all()
        for item in orderItems:
            if item.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Order Items"

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return self.address
