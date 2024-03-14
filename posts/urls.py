from django.urls import path
from .views import post_list,post_detail,delete_post,add_post,comment_list,comment_detail,delete_comment,edit_post,add_comment,edit_comment
from .view2 import PostList,PostDetail,AddPost,EditPost,DeletePost,Commentlist,Commentdetail,DeleteComment,AddComment


app_name = 'posts'

 # blog/
urlpatterns = [
    # blog
    path('', post_list , name='list_post'),
    path('detail/<int:id>', post_detail, name = 'detail'),
    path('detail/<int:id>/delete', delete_post , name='delete'),
    path('add', add_post),
    path('detail/<int:id>/edit', edit_post, name = 'edit'),
 

    # CBV 
    path('cbv/', PostList.as_view(), name='post_list'),
    path('cbv/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('cbv/add', AddPost.as_view()),
    path('cbv/<int:pk>/edit', EditPost.as_view()),
    path('cbv/<int:pk>/delete', DeletePost.as_view(), name='post_delete'),
    path('cbv/comment/list', Commentlist.as_view()),
    path('cbv/<int:pk>/detail', Commentdetail.as_view()),
    path('cbv/<int:pk>/delete', DeleteComment.as_view()),
    path('cbv/addcomment',AddComment.as_view()),
    # comment
    path('comment/',comment_list),
    path('comment/detail/<int:pk>',comment_detail),
    path('comment/detail/<int:pk>/delete',delete_comment),
    path('comment/add',add_comment),
    path('comment/detail/<int:pk>/edit',edit_comment),



]