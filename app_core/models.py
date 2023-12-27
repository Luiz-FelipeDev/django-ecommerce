from django.db import models
from django.contrib.auth.models import (AbstractUser)
from django.conf import settings
from django.urls import reverse

class User(AbstractUser):
    ''' Usuário comum que posso Personalizar '''
    def __str__(self):
        return self.username

CATEGORY_CHOICES = (
    ('P', 'People'),
    ('W', 'Watches'),
    ('CM', 'Cinema'),
    ('CH', 'Clothes'),
    ('H', 'Home items'),
    ('A', 'Animals'),
    
)

LABEL_CHOICES = (
    ('S', 'success'),
    ('P', 'primary'),
    ('D', 'danger'),
    
)



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category_item = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label_item = models.CharField(choices = LABEL_CHOICES, max_length=2)
    slug_item = models.SlugField()
    
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            "app_core:product-detail", 
            kwargs={"slug": self.slug_item}
        )
    
    
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.item


class Order(models.Model):
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add = True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField()
    
    def __str__(self) -> str:
        return f'{self.user.username} - {self.ordered}'