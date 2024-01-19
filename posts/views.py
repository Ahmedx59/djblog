from django.shortcuts import render,redirect
from .models import Post,Comment



def post_list(request):
    post = Post.objects.all()
    return render(request,'post_list.html',{'blog':post})

def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':post})


def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/blog/')


def comment_list(request):
    comment = Comment.objects.all()
    return render(request,'comment_list.html',{'comment':comment})

def comment_detail(request,id):
    comment = Comment.objects.get(id=id)
    return render(request,'comment_detail.html',{'comment':comment})


def comment_delete(request,id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('/comment/')

