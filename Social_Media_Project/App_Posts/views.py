from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from App_Login.models import UserProfile, Follow
from django.contrib.auth.models import User
from App_Posts.models import Posts, Like

# Create your views here.
@login_required
def home(request):
    following_list=Follow.objects.filter(follower=request.user) #user jake jake follow korche tader list
    posts = Posts.objects.filter(author__in=following_list.values_list('following'))#author jodi following_list er modhhe thake taile posts er vitor chole ashbe
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post',flat=True)
    if request.method == 'GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_Posts/home.html', context={'title':'Home','search':search,'result':result,'posts':posts,'liked_post_list':liked_post_list})
@login_required
def liked(request,pk):
    postss=Posts.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=postss,user=request.user)
    if not already_liked:
        liked_post=Like(post=postss,user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))
@login_required
def unliked(request,pk):
    postss=Posts.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=postss,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))
