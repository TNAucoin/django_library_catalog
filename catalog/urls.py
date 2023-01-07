from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("books/", views, name="books_list"),
    # path("authors/", views, name="authors_list"),
    # path("books/<int:pk>", views, name="books_detail"),
    # path("authors/<int:pk>", views, name="authors_detail"),
]
