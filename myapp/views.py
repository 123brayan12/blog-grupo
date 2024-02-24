from django.views.generic.edit import CreateView, UpdateView 
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 


class BlogUpdateView(UpdateView): 
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
class BlogDeleteView(DeleteView): 
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
