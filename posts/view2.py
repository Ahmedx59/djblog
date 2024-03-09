from django.views import generic

from .models import Post,Commints
from .forms import PostForm , CommentForm





#class_from_post>>>>>>>>>>>>>
class PostList(generic.ListView):
    model = Post # post_list.html  object_list.html
                    # context: post_list  , object_list

class PostDetail(generic.DetailView):
    model = Post # post_detail.html  object_detail.html
                    # context: post  , object
    
class DeletePost(generic.DeleteView):
    model =Post
    success_url = '/blog/cbv'

class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title','content','active','created_at','image']  # '__all__'
    template_name = 'posts/add_post.html'
    success_url = '/blog/cbv'

class EditPost(generic.UpdateView):
    model = Post
    form_class = PostForm
    # fields = ['title','content','active','created_at','image']  # '__all__'
    template_name = 'posts/edit_post.html'
    success_url = '/blog/cbv'


#class_from_comment>>>>>>>>>>>>>\


class Commentlist(generic.ListView):
    model = Commints   # template name : modele_list.html or object_list.html 
                        # context  : modele_list  or object_list       


class Commentdetail(generic.DetailView):
    model = Commints



class DeleteComment(generic.DeleteView):
    model = Commints



class AddComment(generic.CreateView):
    model = Commints
    form_class = CommentForm
    # fields = ['content','post']
    success_url = '/blog/cbv/comment/list'
    