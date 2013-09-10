from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^egs_on_the_side/', include('egs_on_the_side.urls')),
    url(r'^contacts/', include('contacts.urls'))
)
