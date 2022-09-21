from django import forms
from .models import Product, Collection, Review

collections = Collection.objects.all().values_list('name','name')
collections_list = []

for collection in collections:
    collections_list.append(collection)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'subname', 'price', 'description', 'snippet', 'digital', 'collection', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'subname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the complete name here'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required':True }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the product in detail here...'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter and overview of the product here'}),
            'digital': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Enter and overview of the product here'}),
            'collection': forms.Select(choices=collections_list, attrs={'class': 'form-control'}), 
        }


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'subname', 'price', 'description', 'snippet', 'digital', 'collection', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'subname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the complete name here'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required':True }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the product in detail here...'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter and overview of the product here'}),
            'digital': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Enter and overview of the product here'}),
            'collection': forms.Select(choices=collections_list, attrs={'class': 'form-control'}), 
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'review', 'product', 'customer')
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'required':True }),
            'review': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a review'}),
            #'product': forms.Select(attrs={'class': 'form-control'}), 
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'product', 'value':'', 'id':'pdt', 'type':'hidden'}),
            #'customer': forms.Select(attrs={'class': 'form-control'}), 
            'customer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'customer', 'value':'', 'id':'ctm', 'type':'hidden'}),
        }


class UpdateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'review')
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'required':True }),
            'review': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a review'}),
        }


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('name', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
        }


class UpdateCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('name', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
        }


