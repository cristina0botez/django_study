from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'cris.views.home', name='home'),
    # url(r'^cris/', include('cris.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^experiments/', include('experiments.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout')
)
# Add the URL pattern in order to make the static files uploaded by the user
# accessible via the Django server.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
