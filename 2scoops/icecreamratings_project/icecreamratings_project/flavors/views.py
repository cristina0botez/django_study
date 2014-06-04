from braces.views import LoginRequiredMixin

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, CreateView, UpdateView, ListView

from .models import Flavor


class FlavorActionMixin(object):

    @property
    def action(self):
        msg = '{0} is missing action.'.format(self.__class__)
        raise NotImplementedError(msg)

    def form_valid(self, form):
        msg = 'Flavor {0}!'.format(self.action)
        messages.info(self.request, msg)
        return super(FlavorActionMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('flavor_details', kwargs={'pk': self.object.pk})


class FlavorDetailView(LoginRequiredMixin, DetailView):

    model = Flavor


class FlavorCreateView(LoginRequiredMixin, FlavorActionMixin, CreateView):

    model = Flavor
    action = 'created'


class FlavorUpdateView(LoginRequiredMixin, FlavorActionMixin, UpdateView):

    model = Flavor
    template_name = 'flavors/flavor_update.html'
    action = 'updated'


class FlavorListView(ListView):

    model = Flavor

    def get_queryset(self):
        result = super(FlavorListView, self).get_queryset()
        q = self.request.GET.get('q')
        if q is not None:
            result = result.filter(name__icontains=q)
        return result
