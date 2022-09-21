from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView, NoProfileView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')), #without the template_name argument it uses Django's default
    path('password/', PasswordsChangeView.as_view(template_name="registration/change-password.html")),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit_profile_page"),
    #path('no_profile/', NoProfileView.as_view(), name="no_profile"),
    path('no_profile/', views.NoProfileView, name="no_profile"),
    path('create_profile_page/', CreateProfilePageView.as_view(), name="create_profile_page"),

    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), 
        name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
        name="password_reset_confirm"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_completed.html"), 
        name="reset_password_complete"),
]
