from django.contrib import admin
from main.models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'count')
    list_filter = ('course','department')