from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Item


def list_items(request):
    
    context = {
        'items': Item.objects.all()
    }
    
    return render(request, 'index.html', context)

def detail_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    
    context = {
        'item': item
    }
    
    return render(request, 'product-detail.html', context=context)
