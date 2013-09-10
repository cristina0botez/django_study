from django.conf.urls import patterns, url

from .views import (
    PublisherList, PublisherDetail,
    processors_example, processors_example_with_render_2_response
)

urlpatterns = patterns(
    '',
    url(r'^processors_example/$', processors_example),
    url(r'^processors_example_with_render_2_response/$',
        processors_example_with_render_2_response),
    url(r'^publishers/$', PublisherList.as_view(), name='publisher_list'),
    url(r'^publisher/(?P<pk>\d+)/$', PublisherDetail.as_view(), name='publisher_detail')
)
