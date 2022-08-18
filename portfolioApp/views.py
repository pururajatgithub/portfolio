from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Images, Category



# Create your views here.

def index(request):
    category = Category.get_category_list()
    return render(request, 'index.html', {'category': category})

def photos(request):
    category_id = request.GET.get('category')
    print(category_id)
    if category_id:
        images = Images.get_images_list_by_category(category_id)
        return render(request, 'photos.html', {'images': images})
    else:
        raise Http404('No Images Found')
    


