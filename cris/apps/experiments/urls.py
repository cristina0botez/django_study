from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import (
    PublisherList, PublisherDetail, BookList, PublisherBookList, AuthorDetail,
    AuthorList,
    ContactView,
    processors_example, processors_example_with_render_2_response
)

urlpatterns = patterns(
    '',
    url(r'^processors_example/$', processors_example),
    url(r'^processors_example_with_render_2_response/$',
        processors_example_with_render_2_response),
    url(r'^publishers/$', PublisherList.as_view(), name='publisher_list'),
    url(r'^publisher/(?P<pk>\d+)/$', PublisherDetail.as_view(),
        name='publisher_detail'),
    url(r'^books/$', BookList.as_view(), name='book_list'),
    url(r'^books/([\w-]+)/$', PublisherBookList.as_view(),
        name='books_by_publisher'),
    url(r'^authors/$', AuthorList.as_view(), name='author_list'),
    url(r'^authors/(?P<author_id>\d+)/$', AuthorDetail.as_view(),
        name='author_detail'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^thanks/$',
        TemplateView.as_view(template_name='experiments/thanks.html'),
        name='thanks')
)
