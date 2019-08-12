
from django.shortcuts import get_object_or_404, render, redirect

from .models import Post
from .forms import PostForm

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
    form = PostForm(
        request.POST if request.POST else None
    )
    if request.POST:
        if form.is_valid():
            post = form.save()
            return redirect('blog', title=post.title)

    return render(
        request,
        'blog/post_form.html',
        {
            "form": form,
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