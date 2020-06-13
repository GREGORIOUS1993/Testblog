from django.urls import path

from article.views import (PostListView, PostDetailView, 
                          AboutView, PostCreateView, 
                          PostUpdateView, PostDeleteView, 
                          DraftListView, add_comment_to_post,
                          comment_approve, comment_remove,
                          post_publish)

from article import views



urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('about/', AboutView.as_view(), name='about'),

    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),

    path('post/<int:pk>/remove/', PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', DraftListView.as_view(), name='post_draft_list'),

    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/delete/', views.comment_remove, name='comment_delete'),

    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
]