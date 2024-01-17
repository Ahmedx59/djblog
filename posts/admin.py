from django.contrib import admin
from .models import Post,Comment


class SearchPost(admin.ModelAdmin):
    search_fields=['title','content']
    list_filter=['title','content']


admin.site.register(Post,SearchPost)
admin.site.register(Comment)