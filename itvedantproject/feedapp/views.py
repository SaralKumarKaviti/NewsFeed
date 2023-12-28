from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post, Comment, Message, Like
from .forms import PostForm, CommentForm, MessageForm

def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confpassword = request.POST.get('password2')

        if password == confpassword:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            return HttpResponse("Passwords do not match!")
        print(username, email, password, confpassword)

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return HttpResponse("Invalid credentials")

    return render(request, 'login.html')

def FeedPage(request):
    users = User.objects.all()
    posts = Post.objects.all()
    messages = Message.objects.all()
    return render(request, 'feed.html', {'posts': posts, 'users': users,'messages':messages})

def CreatePostPage(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            posts = Post.objects.order_by('-created_on')
            return render(request, 'feed.html', {'form': form, 'posts': posts})
    else:
        form = PostForm()

    posts = Post.objects.all()
    return render(request, 'feed.html', {'form': form, 'posts': posts})

def CreateCommentPage(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post_id = post_id
            new_comment.save()
            return redirect('feed')
    else:
        form = CommentForm()

    return render(request, 'comment.html', {'form': form, 'post_id': post_id})
        

def CreateMessagePage(request, receiver_id):
    receiver = get_object_or_404(User, pk=receiver_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.save()
            return redirect('feed')
    else:
        form = MessageForm()
    return render(request, 'message.html', {'form': form, 'receiver_id': receiver_id})

def DeleteMessagePage(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if message.sender == request.user:
        message.delete()  
    return redirect('feed')    
    
def LikePostPage(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.likes += 1
        post.save()
        return redirect('feed')
    else:
        return redirect('feed')

def DeletePostPage(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.user:
        post.delete()
    return redirect('feed')

def LogoutPage(request):
    logout(request)
    return redirect('login')

