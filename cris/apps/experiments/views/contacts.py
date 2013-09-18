from django.views.generic.edit import FormView

from experiments.forms import ContactForm


class ContactView(FormView):
    template_name = 'experiments/contact.html'
    form_class = ContactForm
    success_url = '/experiments/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)