
from django.views.generic.edit import CreateView, UpdateView 
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, TemplateView, ListView, DetailView 
from django.urls import reverse_lazy 
from .models import Post

class BlogUpdateView(UpdateView): 
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
class BlogDeleteView(DeleteView): 
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    
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

