from django.shortcuts import render,redirect

from .models import Post,Commints
from .forms import PostForm,CommentForm



def post_list(request):
    post = Post.objects.all()
    return render(request,'posts/post_list.html',{'blog':post})

def post_detail(request,id):
    post = Post.objects.get(id=id)
    comment = Commints.objects.filter(post=post)
    return render(request,'posts/post_detail.html',{'object':post,"comments":comment})


def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/blog/cbv/')

 
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
           addForm = form.save(commit=False)
           addForm.user = request.user
           addForm.save()
           return redirect('/blog/cbv/')
    else:
        form = PostForm() 
    return  render(request, "posts/post_add.html",{'form':form})


def edit_post(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/blog/detail/{post.id}')
    else:
        form = PostForm(instance=post)
    return render(request, "posts/post_add.html",{'form':form})










def comment_list(request):
    comment = Commints.objects.all()
    return render(request,'posts/commints_list.html',{'comment':comment})


def comment_detail(request,pk):
    comment = Commints.objects.get(id=pk)
    return render(request,'posts/commeits_detail.html',{'comment':comment})

def delete_comment(request,pk):
    comment = Commints.objects.get(id=pk)
    comment.delete()
    return redirect('/comment/') 

def add_comment(request):
    if request.method == 'POST':
        add = CommentForm(request.POST)
        if add.is_valid():
            form = add.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/blog/cbv/comment/list')
    else:
       add = CommentForm()
    return render(request , 'posts/commentadd.html' , {'add':add})


def edit_comment(request,pk):
    comment = Commints.objects.get(id=pk)
    if request.method == 'POST':
       edit = CommentForm(request.POST,instance=comment)
       if edit.is_valid():
            form = edit.save(commit=False)
            form.user =request.user
            form.save()
            return redirect(f'/blog/cbv/{comment.id}/detail')
    else:
       edit = CommentForm(instance=comment)
    return render(request,'posts/edit_comment.html',{'edit':edit})