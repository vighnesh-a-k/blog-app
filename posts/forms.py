from django import forms
from .models import Article,Comment
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']


class CustomUserRegistrationForm(UserCreationForm):


     class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
    
    