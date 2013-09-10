from django.views.generic import ListView, DetailView

from experiments.models import Publisher, Book


__all__ = ['PublisherList', 'PublisherDetail']


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
