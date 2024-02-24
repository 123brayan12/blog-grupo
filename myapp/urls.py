from .views import hello_world
from django.urls import path
from .views import BlogUpdateView
from .views import BlogDeleteView

urlpatterns = [
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit")
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete")
]

