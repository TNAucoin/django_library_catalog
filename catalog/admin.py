from django.contrib import admin
from .models import Author, Language, Genre, Book, BookInstance


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BookInline]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre", "language")
    inlines = [BookInstanceInline]

    def display_genre(self, obj):
        """Create a string for the Genre for display in the admin panel"""
        return ", ".join(genre.name for genre in obj.genre.all()[:3])

    display_genre.short_description = "Genre"


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ("status", "due_back")
    list_display = ("book", "status", "due_back", "borrower", "id")
    fieldsets = (
        ("Instance Details", {"fields": ("book", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back", "borrower")}),
    )


admin.site.register(Genre)
admin.site.register(Language)
