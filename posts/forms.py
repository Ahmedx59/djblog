from django import forms
from .models import Post,Commints

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title','content','active','created_at','image']  # '__all__'
        exclude = ['user',]




class CommentForm(forms.ModelForm):
    class Meta:
        model = Commints
        # fields = '__all__'
        exclude = ['user']