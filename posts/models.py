from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=5000)
    active=models.BooleanField(default=False)


    def __str__(self):
        return self.title

