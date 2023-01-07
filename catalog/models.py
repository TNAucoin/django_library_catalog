from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):
    """Model representing book genre"""

    name = models.CharField(max_length=200, help_text="Enter a book genre.")

    def __str__(self):
        """String representing the model object"""
        return self.name


class Book(models.Model):
    """Model representing a book"""

    title = models.CharField(max_length=200)
    # FK because a book can only have one author, but an author can write many books
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text="Enter brief summary of the book."
    )
    isbn = models.CharField(
        "ISBN", max_length=13, unique=True, help_text="Enter the book's ISBN number."
    )
    # M2M used because genre can contain many books, and books can cover many genres
    genre = models.ManyToManyField(Genre, help_text="Select genre for this book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns URL to access a detail record for this book"""
        return reverse("book-detail", args=[str(self.id)])


class BookInstance(models.Model):
    """Model representing a specific copy of a book"""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book copy"
    )
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateTimeField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On Loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """String repr model object"""
        return f"{self.id} ({self.book.title})"


class Author(models.Model):
    """Model repr an Author"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        """Returns the URL to access a particular Author instance"""
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        """String for repr the model object"""
        return f"{self.last_name}, {self.first_name}"
