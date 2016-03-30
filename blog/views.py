from .models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
        })
def view_post(request, slug):
    return render_to_response('view_post.html', {
        'categories': Category.objects.all(),
        'post': get_object_or_404(Blog, slug=slug)
        })
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'categories': Category.objects.all(),
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
        })
