from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post




class BlogCreateView(CreateView):
    model=Post
    template_name='Createpost.html'
    fields=["title","author","body"]