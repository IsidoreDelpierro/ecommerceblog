from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView, BlogView, PostListView, AboutView, ProductView, ContactView, UpdateCategoryView, DeleteCategoryView, NewMigrate, CategoryViews#, ShopView, CategoryListFuncView

#app_name="blog"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    #path('store/', ShopView.as_view(), name="store"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('blog/', BlogView.as_view(), name='blog'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<int:pk>/update/', UpdateCategoryView.as_view(), name='update_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<int:pk>/remove', DeleteCategoryView.as_view(), name='delete_category'),
    path('category/<str:cats>/', CategoryViews, name="categorys"),
    path('category/<int:pk>/view/', CategoryView.as_view(), name="category"),
    path('product/<int:pk>/', ProductView.as_view(), name="product"),
    path('category-list/', CategoryListView.as_view(), name="category_list"),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
