from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import AuthorForm
from .models import Publisher, Book, Author, UserAuthorInterest


__all__ = [
    'AuthorList', 'AuthorDetail', 'AuthorCreate', 'AuthorUpdate',
    'AuthorDelete',
    'PublisherList', 'PublisherDetail', 'PublisherDetailsWithBookList',
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


class PublisherDetailsWithBookList(SingleObjectMixin, ListView):
    model = Publisher  # For SingleObjectMixin.get_object.
    paginate_by = 2
    # If not set, it will be set automatically to books/book_list.html because
    # of ListView.
    template_name = 'books/publisher_detail_with_books.html'

    def get(self, request, *args, **kwargs):
        publisher_queryset = self.model.objects.all()
        # The queryset must be provided as a parameter, otherwise the
        # get_queryset() method will be invoked.
        self.object = self.get_object(queryset=publisher_queryset)
        return super(PublisherDetailsWithBookList, self).get(request, *args,
                                                             **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PublisherDetailsWithBookList,
                        self).get_context_data(**kwargs)
        context['publisher'] = self.object
        pages_before = context['page_obj'].number - 1
        context['book_list_start_index'] = pages_before * self.paginate_by + 1
        return context

    def get_queryset(self):
        return self.object.book_set.all()


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
