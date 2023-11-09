from django import forms

class AddNetworkDevice(forms.Form):
    brand = forms.CharField(max_length=32)
    model = forms.CharField(max_length=32)
    product_type = forms.CharField(max_length=32)
    price = forms.IntegerField(required=False)
    description = forms.CharField(max_length=255, required=False)

class AddIoTDevice(forms.Form):
    brand = forms.CharField(max_length=32)
    model = forms.CharField(max_length=32)
    product_type = forms.CharField(max_length=32)
    price = forms.IntegerField(required=False)
    description = forms.CharField(max_length=255, required=False)

class AddHardwareComponent(forms.Form):
    brand = forms.CharField(max_length=32)
    model = forms.CharField(max_length=32)
    product_type = forms.CharField(max_length=32)
    price = forms.IntegerField(required=False)
    description = forms.CharField(max_length=255, required=False)
