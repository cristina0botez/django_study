from django.conf.urls import patterns, include, url

from .views import ListContactView, CreateContactView


urlpatterns = patterns(
    '',
    url(r'^$', ListContactView.as_view(), name='contacts_list'),
    url(r'^new/$', CreateContactView.as_view(), name='contacts_new')
)