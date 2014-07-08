from django.conf.urls import patterns, url

from .views import (
    FlavorDetailView, FlavorCreateView, FlavorUpdateView, FlavorListView,
    IceCreamOrderView, IceCreamStoreListView, IceCreamStoreCreateView,
    IceCreamStoreDetailView, IceCreamStoreUpdateView
)


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', FlavorDetailView.as_view(), name='flavor_details'),
    url(r'^add/$', FlavorCreateView.as_view(), name='flavor_create'),
    url(r'^update/(?P<pk>\d+)/$', FlavorUpdateView.as_view(),
        name='flavor_update'),
    url(r'^order/$', IceCreamOrderView.as_view(), name='flavor_order'),
    url(r'^$', FlavorListView.as_view(), name='flavor_list'),

    url(r'^stores/(?P<pk>\d+)/$', IceCreamStoreDetailView.as_view(),
        name='icstore_details'),
    url(r'^stores/add/$', IceCreamStoreCreateView.as_view(),
        name='icstore_create'),
    url(r'^stores/update/(?P<pk>\d+)/$', IceCreamStoreUpdateView.as_view(),
        name='icstore_update'),
    url(r'^stores/$', IceCreamStoreListView.as_view(), name='icstore_list')
)
