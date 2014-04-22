from braces.views import LoginRequiredMixin

from django.views.generic import DetailView

from .models import Flavor


class FlavorDetailView(LoginRequiredMixin, DetailView):

    model = Flavor
