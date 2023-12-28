"""itvedant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from feedapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('feed/',views.FeedPage,name='feed'),
    path('create_post/', views.CreatePostPage, name='create_post'),
    path('create_message/<int:receiver_id>/', views.CreateMessagePage, name='create_message'),
    path('create_comment/<int:post_id>/', views.CreateCommentPage, name='create_comment'),
    path('like_post/<int:post_id>/', views.LikePostPage, name='like_post'),
    path('delete_post/<int:post_id>/', views.DeletePostPage, name='delete_post'),
    path('delete_message/<int:message_id>',views.DeleteMessagePage,name='delete_message'),
    path('logout/',views.LogoutPage,name='logout')
]
