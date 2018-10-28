from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('post/<str:slug>', views.post_detail, name='detail_page'),
    path('create', views.create_post, name='create_post'),
    path('publish', views.publish_post, name="publish_post")
]
