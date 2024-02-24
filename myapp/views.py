

from django.views.generic.edit import CreateView
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView 

def hello_world (request):
    return HttpResponse("Hello world")

""" 
class BlogDetailView(ListView):
    model = Post
    template_name = "BlogDetail.html" """

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogCreateView(CreateView):
    model=Post
    template_name='Createpost.html'
    fields=["title","author","body"]
