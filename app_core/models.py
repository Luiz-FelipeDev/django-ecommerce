from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    
    
    def __str__(self) -> str:
        return self.title
    
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    


class Order(models.Model):
    pass