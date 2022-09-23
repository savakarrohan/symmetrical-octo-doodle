from django.contrib import admin

# Register your models here.
from .models import Book
# I don't like the current layout
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","price",)

admin.site.register(Book,BookAdmin)