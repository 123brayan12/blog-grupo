from .views import BlogDetailView, BlogListView
from django.urls import path
from .views import BlogCreateView


urlpatterns = [
    path("", BlogListView.as_view(), name='MainSite'),
    path("post/new",BlogCreateView.as_view(),name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(),name="post_detail"),
]

