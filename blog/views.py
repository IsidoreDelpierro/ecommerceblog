from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#from store.utils import cartData
from store.views import Store as Shop
from .models import Category, Post, Comment
from .forms import PostForm, UpdatePostForm, CommentForm, CategoryForm, UpdateCategoryForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import random 

from store.models import Collection, Product
from business.models import Business

# Create your views here.
business = Business.objects.get(id=1)

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

    def generate_banner(self, all_products):
        total_number_of_products = all_products.count() 
        most_recent_product = Product.objects.latest('id')
        loop_counter = most_recent_product.id
        number_of_products_in_banner = 4
        banner = []

        while(len(banner) < number_of_products_in_banner):
            random_number = random.randint(0, total_number_of_products-1)
            if all_products[random_number] not in banner:
                banner.append(all_products[random_number])

        print("Banner Products: ", banner) 
        print("\n\nThe id of the most recent Product is: {}\n".format(loop_counter))
        return banner

    def get_featured_products(self, banner, all_products):
        total_number_of_products = all_products.count() 
        number_of_featured_products = 3
        featured_products = []

        while(len(featured_products) < number_of_featured_products):
            random_number = random.randint(0, total_number_of_products-1)
            if all_products[random_number] not in banner and all_products[random_number] not in featured_products:
                featured_products.append(all_products[random_number])

        print("Featured Products: ", featured_products) 
        return featured_products

    def get_featured_collections(self, all_collections):
        total_number_of_collections = all_collections.count() 
        number_of_featured_collections = 3
        featured_collections = []

        while(len(featured_collections) < number_of_featured_collections):
            random_number = random.randint(0, total_number_of_collections-1)
            if all_collections[random_number] not in featured_collections:
                featured_collections.append(all_collections[random_number])

        print("Featured Products: ", featured_collections) 
        return featured_collections
    
    def get_context_data(self, *args, **kwargs):
        all_categories = Category.objects.all()
        all_posts = Post.objects.all()
        all_collections = Collection.objects.all()
        all_products = Product.objects.all()

        banner = self.generate_banner(all_products)
        featured_products = self.get_featured_products(banner, all_products)
        featured_collections = self.get_featured_collections(all_collections)

        context = super(HomeView, self).get_context_data(*args, **kwargs)       
        context["cat_menu"] = all_categories
        context["collections"] = all_collections
        context["col_menu"] = all_collections 
        context["posts"] = all_posts
        context["products"] = all_products 
        context["banner"] = banner
        context["featured_products"] = featured_products
        context["featured_collections"] = featured_collections
        context["business"] = business

        new_cart = Shop() 
        cart = new_cart.get_cart_items(self.request)
        context["cartItems"] = cart
        return context

    
class NewMigrate(ListView):
    model = Post 
    template_name = "blog/upgradeinprogress.html"

class AboutView(ListView):
    model = Post
    template_name = "blog/about.html"

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class ContactView(ListView):
    model = Post
    template_name = "blog/contact.html"

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(ContactView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class ShopView(ListView):
    model = Post
    template_name = "blog/shop.html"

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(ShopView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class ProductView(DetailView):
    model = Post
    template_name = "blog/product.html"

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class CategoryListView(ListView):
    model = Category
    template_name = "blog/category_list.html"

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        context["cat_menu_list"] = cat_list
        context["business"] = business
        context["cartItems"] = cart
        return context

class CategoryView(DetailView):
    model = Category
    template_name = "blog/categories.html"

    def get_context_data(self, *args, **kwargs):
        this_category = get_object_or_404(Category, id=self.kwargs['pk'])
        posts_in_this_category = Post.objects.filter(category__name=this_category.name)
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["category_posts"] = posts_in_this_category
        context["category"] = this_category
        context["business"] = business
        context["cartItems"] = cart
        return context 

def CategoryViews(request, cats):
    '''
        Remember that we are nolonger using this view
    '''
    #category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    category_posts = Post.objects.filter(category__name=cats.replace('-', ' '))
    #context = {'categories':cats.title().replace('-', ' '), 'category_posts':category_posts}
    print("\ncats is: {}; \nAnd Category Products is: {}".format(cats, category_posts))
    context = {'categories':cats.title().replace('-', ' '), 'category_posts':category_posts, 'category':Category.objects.get(name=cats), 'business':business}
    return render(request, 'blog/categories.html', context)

class BlogView(ListView):
    model = Post
    template_name = "blog/blog.html"

    def popular_posts(self):
        pass 

    def popular_categories(self):
        pass 

    def count_comments(self):
        pass 

    def most_popular_post(self):
        #figure out most liked post 
        liked_posts = Post.objects.filter('total_likes > 0').order_by('-id')
        most_liked_post = liked_posts[0]
        for post in liked_posts:
            if post.total_likes > most_liked_post.total_likes:
                most_liked_post = post  
        return most_liked_post 

    def featured_post(self, all_posts):
        post_count = all_posts.count()
        featured_post = all_posts[0]
        for index, post in enumerate(all_posts):
            if index == random.randint(0, post_count):
                featured_post = post 
            print("Item: #{} = {}".format(index, post)) 
        print("Featured Post: ", featured_post) 
        return featured_post

    def featured_categories(self, featured_post, all_categories):
        featured_categories = []  
        feat_cat = featured_post.category 
        print("Featured Category: ", feat_cat)  

        categories_count = all_categories.count()
        for cat_index, category in enumerate(all_categories):
            if len(featured_categories) < 3: 
                #possible to add a featured category 
                if cat_index == random.randint(0, categories_count):
                    #possible featured category 
                    if category.name != feat_cat.name: 
                        #not yet used 
                        featured_categories.append(category)  
                        print("Most Recent Featured Category!\n{}".format(featured_categories[len(featured_categories)-1]))
                    else: 
                        #already used 
                        print("Category {} already featured".format(category)) 
                        pass 
                else: 
                    #not chosen 
                    print("Category not selected for featuring! Try another time!") 
                    pass 
            else: 
                #featured list full 
                print("Featured Category List is full ")
                break  
        print("All Featured Categories", featured_categories)
        return featured_categories

    def sidebar_posts(self, featured_post, all_posts):
        featured_posts = [] 
        #counter = 0 
        random_number = 0
        post_count = all_posts.count()
        while len(featured_posts) < 4:
            random_number = random.randint(0, post_count-1) 
            if all_posts[random_number] != featured_post:
                featured_posts.append(all_posts[random_number])
                print("The post at this index of all_posts is: {}".format(all_posts[random_number]))
                print("The featured post is: {}".format(featured_post)) 
        print("All Featured Posts", featured_posts) 
        return featured_posts 

    def get_context_data(self, *args, **kwargs):
        all_posts = Post.objects.all().order_by('-id')[0:20] 
        all_categories = Category.objects.all()
        
        all_collections = Collection.objects.all()
        all_products = Product.objects.all()
        
        featured_post = self.featured_post(all_posts) #### FEATURED POST #### 
        featured_categories = self.featured_categories(featured_post, all_categories) #### FEATURED CATEGORIES ####
        sidebar_posts = self.sidebar_posts(featured_post, all_posts)    #### POPULAR POSTS ####
        
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)

        context = super(BlogView, self).get_context_data(*args, **kwargs) 
        #context['categories'] = category_posts
        #context['category_posts'] = category_posts 
        context['posts'] = all_posts
        context['featured_post'] = featured_post
        context['featured_categories'] = featured_categories
        context["cat_menu"] = all_categories
        context['featured_posts'] = sidebar_posts
        context["business"] = business
        context["cartItems"] = cart
        return context 

class PostListView(ListView):
    model = Post 
    template_name = "post_list.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu 
        context["business"] = business
        context["cartItems"] = cart
        return context 

class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/article_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        liked_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = liked_post.total_likes()

        liked = False
        if liked_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        context["business"] = business
        context["cartItems"] = cart
        return context


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog/add_category.html"
    #fields = '__all__'
    #fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

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

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(AddCommentView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "blog/update_post.html"
    #fields = ['title', 'title_tag', 'meta_tag', 'body']

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class UpdateCategoryView(UpdateView):
    model = Category
    form_class = UpdateCategoryForm
    template_name = "blog/update_category.html"

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(UpdateCategoryView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = "blog/delete_category.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        new_cart = Shop()
        cart = new_cart.get_cart_items(self.request)
        context = super(DeleteCategoryView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context
