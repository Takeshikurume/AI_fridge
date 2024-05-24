from django.shortcuts import render
from .models import Post

# Create your views here.
def frontpage(request):
    return render(request, "food/frontpage.html")

def foodpage(request):
    posts = Post.objects.all()
    return render(request, "food/foodpage.html", {"posts": posts})