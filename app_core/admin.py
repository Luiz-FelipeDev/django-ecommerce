from django.contrib import admin
from app_core.models import Order, OrderItem, Item, User

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(User)
