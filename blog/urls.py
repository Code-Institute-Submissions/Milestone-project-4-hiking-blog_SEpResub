from . import views 
from django.urls import path



urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'blog/<int:pk>/update/',
        views.CommentUpdateView.as_view(),
        name='comment_update'),
    path(
        'blog/<int:pk>/delete/',
        views.CommentDeleteView.as_view(),
        name='comment_delete'),
    ]

handler404 = 'blog.views.error_404'
