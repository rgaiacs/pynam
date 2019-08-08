from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<title>/', views.blog, name='blog')
]
