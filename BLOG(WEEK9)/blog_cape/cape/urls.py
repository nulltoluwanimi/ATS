from django.urls import path, include
from . import views
from .api import api_views
# app_name = ''

urlpatterns = [
    path('', views.home, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('register/', views.UserCreate.as_view(), name='user-register'),
    path("add-post/", views.CreateBlog.as_view(), name="add-post"),
    path('all-post/', views.BlogList.as_view(), name='all-post'),
    path('post/<slug:slug>/', views.BlogView.as_view(), name='post'),
    path('authors/', views.BloggersListView.as_view(), name='authors'),
    path('author/<int:pk>/update/',
         views.UpdateUser.as_view(), name='author-update'),
    path('author/<int:pk>/', views.UserDetails.as_view(), name='author-profile'),
    path('archived-post/', views.ArchivedPost.as_view(), name='archived-post'),
    path('<slug:slug>/edit', views.BlogEditDetail.as_view(), name='edit-blog'),
    path('<int:pk>/archive-comment/',
         views.ArchiveComment.as_view(), name='archive-comment'),
    path('post/add-comments/<slug:slug>',
         views.SubmitComment, name='add-comment'),
    path("submit-comment-no-reload/<slug:slug>/",
         views.SubmitCommentWithAjax, name='submit-with-fetch')
]

# api-urls
api_prefix = 'api/v1'

urlpatterns += [
    path(f'{api_prefix}/register', api_views.register_view, name="api-register"),
    path(f'{api_prefix}/login',
         api_views.login_view, name="login"),
    path(f'{api_prefix}/post/<int:pk>/detail',
         api_views.post_detail_view, name="api-post-details"),
    path(f'{api_prefix}/post_list',
         api_views.post_list_view, name="api-post-list"),
    path(f'{api_prefix}/post',
         api_views.post_create_view, name="api-post-create"),
    path(f'{api_prefix}/comment/<int:pk>/',
         api_views.comment_view, name="api-comment-create"),
    path(f'{api_prefix}/comment/<int:pk>/all',
         api_views.comment_list_view, name="api-comment-list"),
]
