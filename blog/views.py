from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

#def home(request):
#    context = {}
#    return render(request, 'blog/home.html', context)

 
class HomeView(ListView):
    model = Post 
    template_name = "blog/home.html" 


class ArticleDetailView(DetailView):
    model = Post 
    template_name = "blog/article_details.html"