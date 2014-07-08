from django import forms

from .models import Flavor, IceCreamStore
from .validators import validate_tasty


class FlavorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FlavorForm, self).__init__(*args, **kwargs)
        self.fields['name'].validators.append(validate_tasty)

    class Meta:
        model = Flavor


class IceCreamOrderForm(forms.Form):

    slug = forms.ChoiceField('Flavors')
    toppings = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(IceCreamOrderForm, self).__init__(*args, **kwargs)
        self.fields['slug'].choices = [
            (f.slug, f.name) for f in Flavor.objects.all()
        ]

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Flavor.objects.get(slug=slug).scoops_remaining <= 0:
            raise forms.ValidationError('Sorry, we are out of that flavor.')
        return slug

    def clean(self):
        cleaned_data = super(IceCreamOrderForm, self).clean()
        slug = cleaned_data.get("slug", "")
        toppings = cleaned_data.get("toppings", "")
        # Silly "too much chocolate" validation example
        has_choco = (u"chocolate" in slug.lower() and
                     u"chocolate" in toppings.lower())
        if has_choco:
            msg = u"Your order has too much chocolate."
            raise forms.ValidationError(msg)
        return cleaned_data


class IceCreamStoreCreateForm(forms.ModelForm):

    class Meta:
        model = IceCreamStore
        fields = ('title', 'block_address')


class IceCreamStoreUpdateForm(IceCreamStoreCreateForm):

    def __init__(self, *args, **kwargs):
        super(IceCreamStoreUpdateForm, self).__init__(*args, **kwargs)
        self.fields['phone'].required = True
        self.fields['description'].required = True

    class Meta(IceCreamStoreCreateForm.Meta):
        fields = ('title', 'block_address', 'phone', 'description')
