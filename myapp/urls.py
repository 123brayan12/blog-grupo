from .views import hello_world, ReadPageView, BlogList, BlogDetailView, BlogListView
from django.urls import path

urlpatterns = [
    path("post/<int:pk>/", ReadPageView.as_view(), name='ReadPage'),
    path("", ReadPageView.as_view(), name='ReadPage'),
    
]

