from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def blog(request, title):
    post = get_object_or_404(
        Post,
        title__iexact=title
    )

    return render(
        request,
        'blog/post.html',
        {
            "post": post,
        }
    )