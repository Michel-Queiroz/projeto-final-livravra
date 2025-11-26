from django.contrib import admin
from .models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Use callables for list_display items to avoid lookup errors during system checks
    # (resolves cases where Django can't resolve string names at import time).
    list_display = ('titulo', 'autor', 'isbn', 'publicacao')
    search_fields = ('titulo', 'nome_autor', 'isbn')
