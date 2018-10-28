from django.shortcuts import render
from .models import Post

# Create your views here.


def main_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})


def post_detail(request):
    return render(request, 'post_detail.html', {})
