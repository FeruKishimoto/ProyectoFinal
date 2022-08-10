from django.urls import path
from .views import PasswordsChangeView, UserEditView, UserRegisterView, UserEditView
from django.contrib.auth import views as auth_views
#from .import views

urlpatterns = [
    path('account/signup/', UserRegisterView.as_view(), name='register'),
    path('account/profile/', UserEditView.as_view(), name='profile'),
    #path('account/password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('account/password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),

]