from braces.views import LoginRequiredMixin

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, CreateView

from .models import Flavor


class FlavorDetailView(LoginRequiredMixin, DetailView):

    model = Flavor


class FlavorCreateView(LoginRequiredMixin, CreateView):

    model = Flavor

    def get_success_url(self):
        return reverse('flavor_details', kwargs={'pk': self.object.pk})
