from django.http import HttpResponse 
from django.shortcuts import redirect 
from django.http import HttpResponseRedirect
from django.urls import reverse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def profile_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if hasattr(request.user, 'profile'):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('create_profile_page'))  
        else: 
            return view_func(request, *args, **kwargs) 
    return wrapper_func 


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('You are not allowed to view this page') 
        return wrapper_func
    return decorator


#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin', 'employee'])
#@login_required
#from django.contrib.auth.decorators import login_required

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None 
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name 
        if group == 'customer':
            return redirect('user-page')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_function


