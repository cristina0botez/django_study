from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Template


__all__ = ['processors_example', 'processors_example_with_render_2_response']


def ip_address_processor(request):
    result = {
        'ip_address': request.META['REMOTE_ADDR'],
        'overridden_value': 'value in processor'
    }
    return result


def processors_example(request):
    t = Template('''
<html>
    <head>
        <title>Processors example with RequestContext and HttpResponse</title>
    </head>
    <body>
        <h2>Processors example with RequestContext and HttpResponse</h2>
        foo: {{ foo }} <br/>
        My IP: {{ ip_address }} <br/>
        Value ocerridden by processor: {{ overridden_value }}
    </body>
</html>''')
    rc = RequestContext(
        request,
        dict_={'foo': 'bar', 'overridden_value': 'initial value'},
        processors=[ip_address_processor]
    )
    return HttpResponse(t.render(rc))


def processors_example_with_render_2_response(request):
    context_data = {'foo': 'bar', 'overridden_value': 'initial value'}
    rc = RequestContext(
        request,
        dict_=context_data,
        processors=[ip_address_processor]
    )
    return render_to_response('processors_example_with_render_2_response.html',
                              context_instance=rc)
