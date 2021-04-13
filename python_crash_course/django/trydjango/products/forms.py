from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='snazzy label',
                            widget=forms.TextInput(
                                attrs={"placeholder": 'im a placeholder'}))

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='')
    description = forms.CharField(required=False)
    price = forms.DecimalField(initial=69.69)
