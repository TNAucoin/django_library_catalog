from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="book-list"),
    path(
        "books/borrowed",
        views.LoanedBooksLibrarianListView.as_view(),
        name="librarian-borrowed",
    ),
    path("books/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    path(
        "books/renew/<uuid:pk>/",
        views.renew_book_librarian,
        name="renew-book-librarian",
    ),
    path("authors/", views.AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="user-borrowed"),
]
