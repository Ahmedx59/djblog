from django.contrib import admin
from .models import Post


class SearchPost(admin.ModelAdmin):
    search_fields=['title','content']
    list_filter=['title','content']


admin.site.register(Post,SearchPost)