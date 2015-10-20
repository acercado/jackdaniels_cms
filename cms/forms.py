from django import forms
from .models import Locations
from .models import Product

class Location_New_Account_Form(forms.ModelForm):

    class Meta:
        model = Locations
        fields = ('name', 'schedule', 'address')


class Location_New_Product_Form(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'info', 'banner')