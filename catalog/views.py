from django.shortcuts import render
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
    num_books_with_ipsum = Book.objects.filter(summary__contains="ipsum").count()

    context = {
        "num_books": num_books,
        "num_book_instances": num_book_instances,
        "num_book_instances_available": num_book_instances_available,
        "num_authors": num_authors,
        "num_genres": num_genres,
        "num_books_with_ipsum": num_books_with_ipsum,
    }

    return render(request, "index.html", context=context)
