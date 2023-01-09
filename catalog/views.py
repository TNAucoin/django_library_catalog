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
    # number of visits from this user from session data
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_books": num_books,
        "num_book_instances": num_book_instances,
        "num_book_instances_available": num_book_instances_available,
        "num_authors": num_authors,
        "num_genres": num_genres,
        "num_visits": num_visits,
    }

    return render(request, "index.html", context=context)


class BookListView(ListView):
    """View for returning all books"""

    model = Book
    template_name = "book_list.html"
    context_object_name = "book_list"
    queryset = Book.objects.all()
    paginate_by = 5


class BookDetailView(DetailView):
    """View for a single book instance"""

    model = Book
    template_name = "book_detail.html"
    context_object_name = "book_detail"


class AuthorDetailView(DetailView):
    """View for a single Author instance"""

    model = Author
    template_name = "author_detail.html"
    context_object_name = "author_detail"


class AuthorListView(ListView):
    """View for list of Author instance"""

    model = Author
    context_object_name = "author_list"
    template_name = "author_list.html"
    paginate_by = 5
