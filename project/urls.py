"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import post_list,comment_list,post_detail,delete_post,comment_detail,comment_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', post_list),
    # path('blog/add', add_post),
    path('blog/detail/<int:id>', post_detail),
    path('blog/detail/<int:id>/delete', delete_post),
    path('comment/',comment_list),
    path('comment/detail/<int:id>',comment_detail),
    path('comment/detail/<int:id>/delete',comment_delete)
]
