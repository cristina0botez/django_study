from django.http import HttpResponse
from django.views.generic import View


def hello_world(request):
    return HttpResponse('Hello, World')


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World - said from a Class Based View')