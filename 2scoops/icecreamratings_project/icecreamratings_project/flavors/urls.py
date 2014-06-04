from django.conf.urls import patterns, url

from .views import (
    FlavorDetailView, FlavorCreateView, FlavorUpdateView, FlavorListView
)


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', FlavorDetailView.as_view(), name='flavor_details'),
    url(r'^add/$', FlavorCreateView.as_view(), name='flavor_create'),
    url(r'^update/(?P<pk>\d+)/$', FlavorUpdateView.as_view(),
        name='flavor_update'),
    url(r'^$', FlavorListView.as_view(), name='flavor_list')
)
