from django.conf.urls import patterns, url

from .views import hello_world, MyView


urlpatterns = patterns(
    '',
    url(r'^func_view/hello_world/$', hello_world),
    url(r'^cbv/hello_world/$', MyView.as_view()),
)
