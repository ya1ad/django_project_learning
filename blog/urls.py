from django.urls import path
from . import views
from .views import PostListView, DetailPostView, CreatePostView, UpdatePostView,DelPostView
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('post/<int:pk>/', DetailPostView.as_view(), name="post-detail"),
    path('post/new/', CreatePostView.as_view(), name="post-create"),
    path('post/update/<int:pk>/', UpdatePostView.as_view(), name="post-update"),
    path('post/del/<int:pk>/', DelPostView.as_view(), name="post-del")
]