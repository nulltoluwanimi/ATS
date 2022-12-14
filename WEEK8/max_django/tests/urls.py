from unicodedata import name
from django.urls import path, include
from . import views
from .api import api_views

app_name = 'tests'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('all-borrowed/', views.LoanedBooksListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian,
         name='renew-book-librarian'),
    path('author/<int:pk>', views.AuthorCreate.as_view(), name='one-author'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/',
         views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/',
         views.AuthorDelete.as_view(), name='author-delete'),
    path('books/add/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/',
         views.BookDelete.as_view(), name='book-delete'),
]

# api-urls
api_prefix = 'api/v1'

urlpatterns += [
    path(f'{api_prefix}/register', api_views.register_view, name="api-register"),
    path(f'{api_prefix}/library_details',
         api_views.home_views, name="api-library-details"),
    path(f'{api_prefix}/book_list',
         api_views.book_list_view, name="api-book-list"),
    path(f'{api_prefix}/author_list',
         api_views.author_list_view, name="api-author-list"),
]
