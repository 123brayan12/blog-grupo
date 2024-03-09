from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Post
from django.views.generic import TemplateView, ListView, DetailView 
from django.urls import reverse_lazy

def hello_world (request):
    return HttpResponse("Hello world")

 
class BlogDetailView(DetailView):
    model = Post
    template_name = "BlogDetail.html" 

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogCreateView(CreateView):
    model=Post
    template_name='Createpost.html'
    fields=["title","author","body"]

class BlogDeleteView(DetailView):
    model=Post
    template_name="delete.html"
    success_url=reverse_lazy("home")