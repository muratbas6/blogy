from django.shortcuts import render
from .models import Post
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def main_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})


def post_detail(request):
    return render(request, 'post_detail.html', {})


@staff_member_required
def create_post(request):
    return render(request, 'create.html', {})
