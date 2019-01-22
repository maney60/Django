from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    return render(request,'Blogs/post_list.html',{})


def index(request):
    posts=Post.objects.all()
    context={'posts': posts}
    return render(request,"Blogs/post_list.html",context)

