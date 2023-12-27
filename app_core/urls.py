from django.urls import path
from .views import list_items, detail_item
app_name = 'app_core'

urlpatterns = [
    path('', list_items, name='home-view'),
    path('product/<slug>/', detail_item, name= 'product-detail')
]