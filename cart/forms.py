from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Cantidad',
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    size = forms.ChoiceField(
        choices=[],
        label='Talla',
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)
        if product and hasattr(product, 'sizes') and product.sizes:
            self.fields['size'].choices = [(str(s), f'EU {s}') for s in product.sizes]
        elif product:
            self.fields['size'].choices = [('39', 'EU 39'), ('40', 'EU 40'), ('41', 'EU 41'), ('42', 'EU 42')]
        else:
            self.fields['size'].choices = [('40', 'EU 40')]
