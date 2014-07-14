from braces.views import LoginRequiredMixin

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, CreateView, UpdateView, ListView, FormView
)

from .forms import (
    FlavorForm, IceCreamOrderForm, IceCreamStoreCreateForm,
    IceCreamStoreUpdateForm
)
from .models import Flavor, IceCreamStore


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


class NameSearchMixin(object):

    def get_queryset(self):
        result = super(NameSearchMixin, self).get_queryset()
        q = self.request.GET.get('q')
        if q is not None and q != '':
            result = result.filter(name__icontains=q)
        return result


class FlavorDetailView(LoginRequiredMixin, DetailView):

    model = Flavor


class FlavorCreateView(LoginRequiredMixin, FlavorActionMixin, CreateView):

    model = Flavor
    action = 'created'
    form_class = FlavorForm


class FlavorUpdateView(LoginRequiredMixin, FlavorActionMixin, UpdateView):

    model = Flavor
    template_name = 'flavors/flavor_update.html'
    action = 'updated'
    form_class = FlavorForm


class FlavorListView(NameSearchMixin, ListView):

    model = Flavor


class IceCreamOrderView(FormView):

    template_name = 'flavors/order.html'
    form_class = IceCreamOrderForm

    def form_valid(self, form):
        flavor = Flavor.objects.get(slug=form.cleaned_data['slug'])
        flavor.scoops_remaining -= 1
        flavor.save()
        return super(IceCreamOrderView, self).form_valid(form)

    def get_success_url(self):
        return reverse('flavor_list')


class IceCreamStoreDetailView(DetailView):

    model = IceCreamStore


class IceCreamStoreCreateView(CreateView):

    model = IceCreamStore
    form_class = IceCreamStoreCreateForm

    def get_success_url(self):
        return reverse('icstore_details', kwargs={'pk': self.object.pk})


class IceCreamStoreUpdateView(UpdateView):

    model = IceCreamStore
    template_name = 'flavors/icecreamstore_update.html'
    form_class = IceCreamStoreUpdateForm

    def get_success_url(self):
        return reverse('icstore_details', kwargs={'pk': self.object.pk})


class IceCreamStoreListView(NameSearchMixin, ListView):

    model = IceCreamStore
