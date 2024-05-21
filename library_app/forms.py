from django import forms
from .models import Book, Author, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'category', 'author']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UsernameChangeForm(forms.Form):
    new_username = forms.CharField(label="New Username", widget=forms.TextInput(attrs={'class': 'form-control'}))

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))