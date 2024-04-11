from django import forms

class AddDevice(forms.Form):
    brand = forms.CharField(max_length=32)
    model = forms.CharField(max_length=32)
    product_type = forms.CharField(max_length=32)
    price = forms.IntegerField(required=False)
    description = forms.CharField(max_length=255, required=False, widget=forms.Textarea)

class AddNetworkDevice(AddDevice):
    pass

class AddIoTDevice(AddDevice):
    pass

class AddHardwareComponent(AddDevice):
    pass

class Search(forms.Form):
    input = forms.CharField(max_length=64, required=False, widget=forms.TextInput(attrs={'class': 'form-control bg-light border-0 small', 'id':'search','placeholder':'Buscar'}))

class UpdateDevice(AddDevice):
    pass