from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Book, BookInstance, Genre

# Create your views here.
def index(request):
    """View for homepage"""
    # Generate counts for library objects
    num_books = Book.objects.all().count()
    num_book_instances = BookInstance.objects.all().count()
    num_book_instances_available = BookInstance.objects.filter(
        status__exact="a"
    ).count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()

    context = {
        "num_books": num_books,
        "num_book_instances": num_book_instances,
        "num_book_instances_available": num_book_instances_available,
        "num_authors": num_authors,
        "num_genres": num_genres,
    }

    return render(request, "index.html", context=context)


class BookListView(ListView):
    """View for returning all books"""

    model = Book
    template_name = "book_list.html"
    context_object_name = "book_list"
    queryset = Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book_detail"
