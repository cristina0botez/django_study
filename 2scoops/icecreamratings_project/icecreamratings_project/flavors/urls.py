from django.conf.urls import patterns, url

from .views import FlavorDetailView, FlavorCreateView


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', FlavorDetailView.as_view(), name='flavor_details'),
    url(r'^add/$', FlavorCreateView.as_view(), name='flavor_create')
)
