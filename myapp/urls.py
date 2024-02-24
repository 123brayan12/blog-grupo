from .views import BlogListView, BlogListView
from django.urls import path
from .views import BlogCreateView

urlpatterns = [
    path("", BlogListView.as_view(), name='ReadPage'),
    path("post/new",BlogCreateView.as_view(),name="post_new"),
]

