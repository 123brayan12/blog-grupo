from .views import hello_world, ReadPageView
from django.urls import path

urlpatterns = [
    path("", ReadPageView.as_view(), name='ReadPageMain'),
    
]

