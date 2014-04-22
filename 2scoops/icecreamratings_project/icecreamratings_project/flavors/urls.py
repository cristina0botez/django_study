from django.conf.urls import patterns, url

from .views import FlavorDetailView


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', FlavorDetailView.as_view())
)
