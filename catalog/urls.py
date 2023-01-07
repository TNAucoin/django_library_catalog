from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("books/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    # path("authors/", views, name="authors_list"),
    # path("authors/<int:pk>", views, name="authors_detail"),
]
