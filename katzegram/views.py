from django.shortcuts import render, redirect
from . forms import SignUpForm, PostForm
from . models import Post, Profile, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
import random

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        
        profile = Profile.objects.exclude(user=request.user)

        comments = Comment.objects.all().order_by('-created_at')
        posts = Post.objects.all().order_by('-created_at') 
        return render(request, 'home.html',{"posts":posts,'profile':profile,'comments':comments})
    else:
        return render(request, 'login.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,('error logging in!!!!'))
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,('you have been pursued'))
    return render(request, 'login.html')


def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password1'] 
            user = authenticate(username=username, password=password)
            return redirect('home')
        
    return render(request, 'register.html',{'form':form})

def profile(request, pk):

    posts = Post.objects.filter(user_id=pk)
    profile = Profile.objects.get(user_id=pk)
    # pro = Profile.objects.get(user_id=pk).order_by(?)
    return render(request, 'profile.html',{'profile':profile, 'posts':posts})

def create(request):
    if request.user.is_authenticated:
        post_form = PostForm(request.POST or None, request.FILES or None)
        if request.method == 'POST':
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('home')
        return render(request, 'create.html',{'post_form':post_form})

    else:
        return render(request,'login.html')
    