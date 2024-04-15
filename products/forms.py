from django import forms

class AddDevice(forms.Form):
    brand = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'brand','placeholder':'Marca'}))
    model = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'model','placeholder':'Modelo'}))
    product_type = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'product_type','placeholder':'Categoria'}))
    price = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'price','placeholder':'Precio'}))
    description = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'id':'description','placeholder':'Descripcion'}))
    def __init__(self,*args, **kwargs):
        super(AddDevice, self).__init__(*args, **kwargs)
        self.fields['brand'].label = ''
        self.fields['model'].label = ''
        self.fields['product_type'].label = ''
        self.fields['price'].label = ''
        self.fields['description'].label = ''

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