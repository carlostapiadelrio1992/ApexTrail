from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'postal_code', 'payment_method']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full bg-neutral-800 border border-neutral-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:border-amber-500',
                'placeholder': 'Ej. Juan'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full bg-neutral-800 border border-neutral-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:border-amber-500',
                'placeholder': 'Ej. Pérez'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-neutral-800 border border-neutral-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:border-amber-500',
                'placeholder': 'ejemplo@apextrail.cl'
            }),
            'address': forms.TextInput(attrs={
                'class': 'w-full bg-neutral-800 border border-neutral-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:border-amber-500',
                'placeholder': 'Av. Principal #123, Depto 4B'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full bg-neutral-800 border border-neutral-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:border-amber-500',
                'placeholder': 'Santiago / Providencia'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'w-full bg-neutral-800 border border-neutral-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:border-amber-500',
                'placeholder': '7500000'
            }),
            'payment_method': forms.Select(attrs={
                'class': 'w-full bg-neutral-800 border border-neutral-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:border-amber-500'
            }),
        }
