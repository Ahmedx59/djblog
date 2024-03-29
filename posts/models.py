from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_post')
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=5000)
    active=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to="post")


    def __str__(self):
        return self.title

class Commints(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_commint')

    def __str__(self):
        return str(self.user)    
