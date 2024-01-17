from django.shortcuts import render
from .models import Post,Comment



def post_list(request):
    post = Post.objects.all()
    return render(request,'post_list.html',{'blog':post})


def comment_list(request):
    comment = Comment.objects.all()
    return render(request,'comment_list.html',{'comment':comment})