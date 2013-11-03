from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from experiments.forms import AuthorForm
from experiments.models import Publisher, Book, Author, UserAuthorInterest


__all__ = [
    'AuthorList', 'AuthorDetail', 'AuthorCreate', 'AuthorUpdate',
    'AuthorDelete',
    'PublisherList', 'PublisherDetail',
    'BookList', 'PublisherBookList',
    'RecordInterest'
]


class AuthorList(ListView):
    model = Author


class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'author'
    pk_url_kwarg  = 'author_id'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorDetail, self).dispatch(*args, **kwargs)

    def get_object(self):
        author = super(AuthorDetail, self).get_object()
        author.last_accessed = timezone.now()
        author.save()
        return author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        context['user_access_count'] = (
            UserAuthorInterest.get_interest_of_user_in_author(
                self.request.user,
                context['author']
            )
        )
        return context


class AuthorCreate(CreateView):
    form_class = AuthorForm
    model = Author
    context_object_name = 'author'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AuthorCreate, self).form_valid(form)


class AuthorUpdate(UpdateView):
    form_class = AuthorForm
    model = Author
    context_object_name = 'author'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorUpdate, self).dispatch(*args, **kwargs)


class AuthorDelete(DeleteView):
    model = Author
    context_object_name = 'author'
    success_url = reverse_lazy('author_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorDelete, self).dispatch(*args, **kwargs)


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


class RecordInterest(View, SingleObjectMixin):
    """Records the current user's interest in an author."""
    model = Author

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecordInterest, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        UserAuthorInterest.increment_interest_of_user_in_author(
            self.request.user, self.object
        )
        return HttpResponseRedirect(reverse('author_detail',
                                    kwargs={'author_id': self.object.pk}))
