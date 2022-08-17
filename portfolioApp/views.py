from django.shortcuts import render
from django.http import HttpResponse
from .models import Images, Category



# Create your views here.

def index(request):
    category = Category.get_category_list()
    return render(request, 'index.html', {'category': category})

def images(request, category_id):
    images = Images.get_images_list_by_category(category_id)
    return render(request, 'images.html', {'images': images})


