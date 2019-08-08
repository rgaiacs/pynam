from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    return render(
        request,
        'blog/index.html',
        {}
    )

def blog(request, title):
    post = Post.objects.get(
        title__iexact=title
    )

    print(post)

    return render(
        request,
        'blog/post.html',
        {
            "post": post,
        }
    )