from django.utils import timezone
from django.views.generic import ListView, DetailView

from experiments.models import Publisher, Book, Author


__all__ = ['PublisherList', 'PublisherDetail', 'BookList', 'PublisherBookList',
           'AuthorDetail', 'AuthorList']


class AuthorList(ListView):
    model = Author


class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'author'
    pk_url_kwarg  = 'author_id'

    def get_object(self):
        author = super(AuthorDetail, self).get_object()
        author.last_accessed = timezone.now()
        author.save()
        return author


class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'books'


class PublisherBookList(ListView):
    context_object_name = 'books'
    template_name = 'experiments/books_by_publisher.html'

    def get_queryset(self):
        # self will contain: request, args and kwargs
        books = Book.objects.filter(publisher__name=self.args[0])
        return books

    def get_context_data(self, **kwargs):
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        context['publisher'] = self.args[0]
        return context


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publishers'


class PublisherDetail(DetailView):
    model = Publisher
    context_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context
