from django import forms
from .models import Post, Category

#choices = [('powerbike','Power Bike'), ('scooter','Scooter'),('skateboard','Skate Board'),]
choices = Category.objects.all().values_list('name','name')
choices_list = []

for choice in choices:
    choices_list.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'meta_tag', 'author', 'category', 'body', 'snippet', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Text entered here will appear as the name of the tab in the browser'}),
            'meta_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name', 'value':'', 'id':'root', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the blog post goes here...'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter snippet here'}),
        }


class UpdatePostForm(forms.ModelForm):
    '''
        In views.AddPostView() and views.UpdatePostView() we took off the fields attribute.
        It can't be used alongside the form_class attribute which we need in order to style with Bootstrap.
        We do not want the author of a blog post to be editable, so we're creating this form to handle that.
    '''
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'meta_tag', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Text entered here will appear as the name of the tab in the browser'}),
            'meta_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the blog post goes here...'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Content of the blog post goes here...'}),
        }
