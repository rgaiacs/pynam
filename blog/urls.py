from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog_form, name='blog_form'),
    path('blog/<title>/', views.blog, name='blog')
]
