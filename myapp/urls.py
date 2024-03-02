from .views import BlogDetailView, BlogListView
from django.urls import path

urlpatterns = [
    path("", hello_world, name='helloworld'),
]

