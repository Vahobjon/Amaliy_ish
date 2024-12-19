from django.shortcuts import render
from .models import *

# Create your views here.

def home(requests):
    ctg = Category.objects.all()
    sneaker = Sneakers.objects.all()
    ctx = {
        'ctg': ctg,
        'sneaker': sneaker
    }
    return render(requests, 'blog/index.html', ctx)


def contact(requests):
    ctx = {}
    return render(requests, 'blog/contact.html', ctx)


def products(requests, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    sneaker = Sneakers.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg': ctg,
        'category': category,
        'sneaker': sneaker
    }
    return render(requests, 'blog/products.html', ctx)


def register(requests):
    ctx = {}
    return render(requests, 'blog/register.html', ctx)


def single(requests):
    ctx = {}
    return render(requests, 'blog/single.html', ctx)