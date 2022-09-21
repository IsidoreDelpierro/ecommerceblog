from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from members.models import Profile as Customer
from .models import *
from .forms import ProductForm, UpdateProductForm, CollectionForm, UpdateCollectionForm, ReviewForm, UpdateReviewForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import json
import datetime
from .utils import cartData, guestOrder
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from blog.decorators import profile_required 
from django.core.paginator import Paginator, EmptyPage
from business.models import Business

# Create your views here.
business = Business.objects.get(id=1)

class Store(ListView):
    model = Product
    template_name = "store/store.html"
    ordering = ['-id']
    cartData = cartData 

    def get_cart_items(self, given_request):
        data = cartData(given_request)
        cartItems = data['cartItems']
        return cartItems

    def get_context_data(self, *args, **kwargs):
        data = self.cardData(self.request)
        cartItems = data['cartItems']
        print("\n\nCart Items: {}".format(cartItems))

        products = Product.objects.all().order_by('-d')
        collections = Collection.objects.all().order_by('-id')
        
        context = super(Store, self).get_context_data(*args, **kwargs)
        context["products"] = products
        context["collections"] = collections
        context["business"] = business
        context["cartItems"] = cartItems
        return context

def paginate_queryset(request, query_list, items_per_page):
    paginated_query = Paginator(query_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        paginated_query_list = paginated_query.page(page_number) 
    except EmptyPage:
        paginated_query_list = paginated_query.page(1) 
    return paginated_query_list, page_number  

@profile_required
def StoreView(request):
    data = cartData(request)
    cartItems = data['cartItems']
    collections = Collection.objects.all()
    products, page_number = paginate_queryset(request, Product.objects.all().order_by('-id'), 9)
    context = {'products':products, 'page':page_number, 'collections':collections, 'business':business, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

@profile_required
def ProductListView(request):
    all_products = Product.objects.all().order_by('-id')
    new_cart = Store()
    cart = new_cart.get_cart_items(request)
    context = {'products':all_products, 'business':business, 'cartItems':cart}
    return render(request, 'store/products.html', context) 

@profile_required
def ProductView(request, pk):
    all_products = Product.objects.all()
    this_product = Product.objects.get(id=pk)
    this_product_versions = Version.objects.filter(product__name=this_product.name)
    related_products = Product.objects.filter(collection__name=this_product.collection)
    product_reviews = this_product.review_set.all()
    print("Reviews for {}: \n{}".format(this_product.name, product_reviews))
    product_reviews, page_number = paginate_queryset(request, this_product.review_set.all().order_by('-id'), 2)

    print(all_products)
    print(this_product)
    print("\n\nProduct Versions: {}".format(this_product_versions))
    print("\n\nRelated Products: {}".format(related_products))

    new_cart = Store()
    cart = new_cart.get_cart_items(request)

    context = {
        'all_products':all_products, 'product':this_product, 'business':business,
        'versions':this_product_versions, 'related':related_products, 
        'reviews':product_reviews, 'page':page_number, 'cartItems':cart,
        }
    return render(request, 'store/product.html', context) 

def CollectionListView(request):
    all_collections = Collection.objects.all()
    new_cart = Store()
    cart = new_cart.get_cart_items(request)
    context = {'collections':all_collections, 'business':business, 'cartItems':cart} 
    return render(request, 'store/collections.html', context)

@profile_required
def CollectionView(request, pk):
    all_collections = Collection.objects.all()
    this_collection = Collection.objects.get(id=pk)
    this_collection_products = Product.objects.filter(collection__name=this_collection.name)
    #this_collection_products = this_collection.product_set()

    print("All Collections: ", all_collections)
    print("This Collection: ", this_collection)
    print("These Products: ", this_collection_products)

    new_cart = Store()
    cart = new_cart.get_cart_items(request)

    context = {
        'collections':all_collections, 'collection':this_collection, 
        'products':this_collection_products, 'business':business, 
        'cartItems':cart}
    return render(request, 'store/collection.html', context) 

@profile_required
def ProductsView(request, pk):
    all_collections = Collection.objects.all()
    this_collection = Collection.objects.get(id=pk)
    this_collection_products, page_number = paginate_queryset(request, Product.objects.filter(collection__name=this_collection.name), 9)
    new_cart = Store()
    cart = new_cart.get_cart_items(request)
    context = {
        'collections':all_collections, 'collection':this_collection, 
        'products':this_collection_products, 'page':page_number,
        'business':business, 'cartItems':cart,}
    return render(request, 'store/store.html', context) 

class AddCollectionView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = "store/add_collection.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        new_cart = Store()
        cart = new_cart.get_cart_items(self.request)
        context = super(AddCollectionView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class UpdateCollectionView(UpdateView):
    model = Collection
    form_class = UpdateCollectionForm
    template_name = "store/update_collection.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        new_cart = Store()
        cart = new_cart.get_cart_items(self.request)
        context = super(UpdateCollectionView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class DeleteCollectionView(DeleteView):
    model = Collection
    template_name = "store/delete_collection.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        new_cart = Store()
        cart = new_cart.get_cart_items(self.request)
        context = super(DeleteCollectionView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "store/add_product.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        new_cart = Store()
        cart = new_cart.get_cart_items(self.request)
        context = super(AddProductView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class UpdateProductView(UpdateView):
    model = Product
    form_class = UpdateProductForm
    template_name = "store/update_product.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        new_cart = Store()
        cart = new_cart.get_cart_items(self.request)
        context = super(UpdateProductView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class DeleteProductView(DeleteView):
    model = Product
    template_name = "store/delete_product.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        new_cart = Store()
        cart = new_cart.get_cart_items(self.request)
        context = super(DeleteProductView, self).get_context_data(*args, **kwargs)
        context["business"] = business
        context["cartItems"] = cart
        return context

class AddReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "store/add_review.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        product_to_review = get_object_or_404(Product, id=self.kwargs['pk'])
        customer_making_review = get_object_or_404(Customer, id=self.request.user.profile.id)
        context = super(AddReviewView, self).get_context_data(*args, **kwargs)
        new_cart = Store()
        cart = new_cart.get_cart_items(self.request)
        context["product"] = product_to_review
        context["customer"] = customer_making_review
        context["business"] = business
        return context

class UpdateReviewView(UpdateView):
    model = Review
    form_class = UpdateReviewForm
    template_name = "store/update_review.html"
    success_url = reverse_lazy('home')
    
class DeleteReviewView(DeleteView):
    model = Review
    template_name = "store/delete_review.html"
    success_url = reverse_lazy('home')
    
def CartView(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'business':business, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def CheckOutView(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'business':business, 'order':order, 'items':items, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def UpdateItemView(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductId:', productId)

    customer = request.user.profile
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def ProcessOrderView(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.profile 
        print("\nBig shout out to you all the way from ProcessOrderView. \nEat this middle finger from {}. \nBitch! I am authenticated!\n".format(customer))
        order, created = Order.objects.get_or_create(customer=customer, complete=False)



    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    received_total = float(order.get_cart_total)

    print("Total is: {}".format(total))
    print("Received Total is: {}".format(received_total))

    if total == received_total:
        order.complete = True
        print("\n\nAnd now the order is complete\n")
    order.save()
    print("\n\nWe just saved order: {}".format(order))

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete!', safe=False)
