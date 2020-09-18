from django import forms
from .models import listing_model
class listing_form(forms.ModelForm):
    class Meta:
        model = listing_model
        fields = ['title', 'address', 'city', 'state', 'price', 'pincode', 'sqfoot', 'rooms', 'image', 'phone']