from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1', 'password2')

    def __init__(self, *args, **kwargs): #se hace de esta manera porque estoy con la autenticidad importada.
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #direccion_web = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password2 = forms.CharField(label='Repetir Password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #imagen = forms.ImageField()
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password',)

