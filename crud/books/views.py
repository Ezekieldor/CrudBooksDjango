from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book

class IndexView(generic.ListView):
    template_name = 'books/index.html'
    model = Book

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

class CreateView(CreateView):
    model = Book
    fields = ['name', 'pages']
    template_name = 'books/create.html'
    success_url = reverse_lazy('books:index')

class UpdateView(generic.DetailView):
    model = Book
    template_name = 'books/update.html'

class DeleteView(DeleteView):
    model = Book
    template_name = 'books/delete.html' 

def create_book (request):
    book = Book(name = request.POST['bookName'], pages = request.POST['bookPages'])
    book.save()
    return HttpResponseRedirect(reverse('books:index'))

def update_book (request):
    c = Book.objects.filter(name = request.POST['bookName'])
    c.delete()
    book = Book(name = request.POST['bookName'], pages = request.POST['bookPages'])
    book.save()
    return HttpResponseRedirect(reverse('books:index'))

def delete_book (request):
    c = Book.objects.filter(name = request.POST['nameDelete'])
    c.delete()
    return HttpResponseRedirect(reverse('books:index'))

