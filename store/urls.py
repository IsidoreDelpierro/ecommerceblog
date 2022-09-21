from django.urls import path 
from . import views

#app_name="store"

urlpatterns = [
    path('', views.StoreView, name="store"),
    path('collection/<int:pk>/', views.ProductsView, name="catalog"),
    path('cart/', views.CartView, name="cart"),
    path('checkout/', views.CheckOutView, name="checkout"),

    path('update_item/', views.UpdateItemView, name="update_item"),
    path('process_order/', views.ProcessOrderView, name="process_order"),

    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('product/<int:pk>/edit/', views.UpdateProductView.as_view(), name='update_product'),
    path('product/<int:pk>/remove/', views.DeleteProductView.as_view(), name='delete_product'),

    path('add_collection/', views.AddCollectionView.as_view(), name='add_collection'),
    path('collection/<int:pk>/edit/', views.UpdateCollectionView.as_view(), name='update_collection'),
    path('collection/<int:pk>/remove/', views.DeleteCollectionView.as_view(), name='delete_collection'),

    #path('product/<int:pk>/review/', views.ReviewView, name='review'),
    path('add_review/<int:pk>/', views.AddReviewView.as_view(), name='add_review'),
    path('review/<int:pk>/edit/', views.UpdateReviewView.as_view(), name='update_review'),
    path('review/<int:pk>/remove/', views.DeleteReviewView.as_view(), name='delete_review'),

    path('product/<int:pk>/', views.ProductView, name="product_detail"),
    path('products/', views.ProductListView, name="product_list"),
    path('collection/<int:pk>/', views.CollectionView, name="collection"),
    path('collections/', views.CollectionListView, name="collection_list"),
]
