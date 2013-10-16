from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import (
    AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete,
    PublisherList, PublisherDetail,
    BookList, PublisherBookList,
    ContactView,
    processors_example, processors_example_with_render_2_response
)

urlpatterns = patterns(
    '',
    # processors
    url(r'^processors_example/$', processors_example),
    url(r'^processors_example_with_render_2_response/$',
        processors_example_with_render_2_response),

    # books (book-author-publisher examples)
    url(r'^publishers/$', PublisherList.as_view(), name='publisher_list'),
    url(r'^publisher/(?P<pk>\d+)/$', PublisherDetail.as_view(),
        name='publisher_detail'),
    url(r'^books/$', BookList.as_view(), name='book_list'),
    url(r'^books/([\w-]+)/$', PublisherBookList.as_view(),
        name='books_by_publisher'),
    url(r'^authors/$', AuthorList.as_view(), name='author_list'),
    url(r'^authors/(?P<author_id>\d+)/$', AuthorDetail.as_view(),
        name='author_detail'),
    url(r'^authors/add/$', AuthorCreate.as_view(), name='author_create'),
    url(r'^authors/(?P<pk>\d+)/update/$', AuthorUpdate.as_view(),
        name='author_update'),
    url(r'^authors/(?P<pk>\d+)/delete/$', AuthorDelete.as_view(),
        name='author_delete'),

    # contacts (address book examples)
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^thanks/$',
        TemplateView.as_view(template_name='experiments/thanks.html'),
        name='thanks')
)
