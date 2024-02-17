from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView 
from .models import Post

def hello_world (request):
    return HttpResponse("Hello world")

class BlogListView(ListView):
    model = Post
    template_name = "ReadMain.html"

class BlogDetailView(ListView):
    model = Post
    template_name = "BlogDetailView.html"

