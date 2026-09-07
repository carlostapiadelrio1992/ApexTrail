from django import forms


class ProductSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'bg-neutral-800 text-white rounded-lg px-4 py-2 w-full focus:outline-none focus:ring-2 focus:ring-amber-500',
            'placeholder': 'Buscar zapatillas, modelos o tecnologías...'
        })
    )
