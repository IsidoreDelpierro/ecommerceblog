from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post, Comment
from .forms import PostForm, UpdatePostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

#def home(request):
#    context = {}
#    return render(request, 'blog/home.html', context)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    #ordering = ['-post_date']
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    context = {'cat_menu_list':cat_menu_list}
    return render(request, 'blog/category_list.html', context)

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    context = {'categories':cats.title().replace('-', ' '), 'category_posts':category_posts}
    return render(request, 'blog/categories.html', context)

class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/article_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        liked_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = liked_post.total_likes()

        liked = False
        if liked_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = "blog/add_category.html"
    fields = '__all__'
    #fields = ('title', 'body')


class AddPostView(CreateView):
    model = Post
    form_class = CommentForm
    template_name = "blog/add_post.html"
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"
    #fields = '__all__'
    ordering = ['-id']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')



class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "blog/update_post.html"
    #fields = ['title', 'title_tag', 'meta_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')
