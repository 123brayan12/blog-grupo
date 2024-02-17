from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def hello_world (request):
    return HttpResponse("Hello world")

class ReadPageView(TemplateView):
    template_name = "ReadMain.html"


