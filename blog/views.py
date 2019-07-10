from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog

def index(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'blogs':blogs, 'posts':posts})

# Create your views here.
