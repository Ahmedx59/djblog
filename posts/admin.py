from django.contrib import admin
from .models import Post,Commints


class SearchPost(admin.ModelAdmin):
    search_fields=['title','content']
    list_filter=['title','content']


admin.site.register(Post,SearchPost)

class search_commint(admin.ModelAdmin):
    search_fields=['content']
    list_filter=['content']

admin.site.register(Commints,search_commint)











