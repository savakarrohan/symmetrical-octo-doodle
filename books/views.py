from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Book

class BookListView(ListView):
    """Generic List view"""
    model = Book
    context_object_name = "book_list"
    template_name: str = "books/book_list.html"
class BookDetailView(DetailView):
    """Generic detail vie of model book"""
    model = Book
    context_object_name = "book_detail"
    template_name: str = "books/book_detail.html"
    