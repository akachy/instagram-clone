from django.shortcuts import render, redirect
from . forms import SignUpForm, PostForm, CommentForm, ProfilePicForm
from . models import Post, Profile, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        profile = Profile.objects.exclude(user=request.user)
        comments = Comment.objects.all().order_by('-created_at')
        posts = Post.objects.all().order_by('-created_at') 
        comment_form = CommentForm(request.POST or None)
        if request.method == 'POST':
            if comment_form.is_valid():
                form = comment_form.save(commit=False)
                form.user = request.user
                
                form.save()
        return render(request, 'home.html',{"posts":posts,'profile':profile,'comments':comments,'comment_form':comment_form})
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
    if request.method == 'POST':
        current_user_profile = request.user.profile
        action = request.POST['follow']
        # decide to follow
        if action == 'unfollow':
            current_user_profile.follows.remove(profile)
        elif action == 'follow':
            current_user_profile.follows.add(profile)
        
        # save profile

        current_user_profile.save()

    
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
    
def post_detail(request, pk):
    posts = get_object_or_404(Post, id=pk)
    comments = Comment.objects.all().order_by('-created_at')
    comment_form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.user = request.user
            form.post = posts
            form.save()
            return JsonResponse({'message':'success'})
        else:
            comment_form = CommentForm()
    return render(request, 'post_detail.html',{'posts':posts,'comment_form':comment_form,'comments':comments})

def settings(request):
    if request.user.is_authenticated:
        profile_user = Profile.objects.get(user__id=request.user.id)

        # get forms
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,('information updated'))
            return redirect('profile',pk = request.user.id)



        return render(request, 'settings.html',{'profile_form':profile_form})

    else:
        messages.success(request,('You gats be logged in !!'))
        return redirect('home')
    



    
