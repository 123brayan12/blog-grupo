from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 
from django.views.generic import TemplateView, ListView, DetailView 
from .models import Post

class BlogUpdateView(UpdateView): 
    model = Post
    template_name = "update.html"
    fields = ["title", "body"]
class BlogDeleteView(DeleteView): 
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("MainSite")
 
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
