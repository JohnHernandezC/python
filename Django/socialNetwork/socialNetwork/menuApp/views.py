from django.shortcuts import render

from .models import *

def menu(request):
    post=Post.objects.all()
    return render(request,'social/feed.html',{'post':post})

def perfiles(request):
    return render(request,'social/profile.html')
