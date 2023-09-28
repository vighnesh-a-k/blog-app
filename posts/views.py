from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.contrib.auth.models import User 
from .models import Article,Comment
from .forms import ArticleForm,CustomUserRegistrationForm,CommentForm

from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm

def post_list(request):
    posts= Article.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Article, id=post_id)
    comments = Comment.objects.filter(article_id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.author = request.user 
            comment.article = post  # Set the article to the current post
            
            comment.save()
            return redirect(request.get_full_path())
    else:
        form = CommentForm()

    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'article_details.html', context) 

def home(request):
	posts= Article.objects.all()
	return render(request, 'index.html', {'posts': posts})


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article =form.save(commit=False) 
            article.author = request.user  # Set the author to the current user
            
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

# User login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a dashboard page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User signup view
def signup(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            
            user=form.save(commit=False)
            user.save()
            return redirect('login')  # Redirect to a dashboard page after signup
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

def delete_post(request, post_id):
    post = get_object_or_404(Article, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'article_delete.html', {'post': post})




def edit_post(request, post_id):
    post = get_object_or_404(Article, id=post_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post_id=post.id)
    else:
        form = ArticleForm(instance=post)
    return render(request, 'create_article.html', {'form': form})


     
