from django.contrib import admin
from p_library.models import Book, Author, Publisher
# from django.contrib.admin import SimpleListFilter


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','publisher',)
    list_filter=('author','publisher',)
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('country',)
    list_display=('full_name','country',)
    pass


