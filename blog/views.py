from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy

# Create your views here.

#def home(request):
#    context = {}
#    return render(request, 'blog/home.html', context)

 
class HomeView(ListView):
    model = Post 
    template_name = "blog/home.html" 
    ordering = ['-post_date']
    #ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post 
    template_name = "blog/article_details.html"


class AddCategoryView(CreateView):
    model = Category 
    #form_class = PostForm
    template_name = "blog/add_category.html"
    fields = '__all__' 
    #fields = ('title', 'body')


class AddPostView(CreateView):
    model = Post 
    form_class = PostForm
    template_name = "blog/add_post.html"
    #fields = '__all__' 
    #fields = ('title', 'body')


class UpdatePostView(UpdateView):
    model = Post 
    form_class = UpdatePostForm
    template_name = "blog/update_post.html"
    #fields = ['title', 'title_tag', 'meta_tag', 'body']


class DeletePostView(DeleteView):
    model = Post 
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')