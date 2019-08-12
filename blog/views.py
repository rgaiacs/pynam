
from django.shortcuts import get_object_or_404, render, redirect

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

def blog_form(request):
    if request.POST:
        post = Post(
            title=request.POST["title"],
            text=request.POST["text"]
        )
        post.save()
        return redirect('blog', title=post.title)

    return render(
        request,
        'blog/post_form.html',
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