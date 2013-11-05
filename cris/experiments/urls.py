from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import (
    ContactView,
    processors_example, processors_example_with_render_2_response
)

urlpatterns = patterns(
    '',
    # processors
    url(r'^processors_example/$', processors_example),
    url(r'^processors_example_with_render_2_response/$',
        processors_example_with_render_2_response),

    # contacts (address book examples)
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^thanks/$',
        TemplateView.as_view(template_name='experiments/thanks.html'),
        name='thanks')
)
