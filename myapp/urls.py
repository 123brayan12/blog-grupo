from django.urls import path
from .views import BlogCreateView


urlpatterns = [
    path("post/new",BlogCreateView.as_view(),name="post_new"),
]

