from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from blog import models;
# Create your views here.
def hello(request):
    return HttpResponse("hello word");

def index(request):
    blog_index = models.Article.objects.all().order_by("id")
    context = {
        'blog_index': blog_index,
    }
    return render(request, 'index.html', context)

def redirect_to_year(request):
    year = 2006
    return HttpResponseRedirect(reverse('news-year-archive', args = (year,)))