from django.shortcuts import render
from .models import Post
from .forms import CreateForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.text import slugify

# Create your views here.


def main_page(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {"posts": posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {"post": post})


@staff_member_required
def create_post(request):
    form = CreateForm()
    return render(request, 'create.html', {"form": form})


@staff_member_required
def publish_post(request):
    form = CreateForm(request.GET)
    if form.is_valid():
        postObject = form.save()

    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})
