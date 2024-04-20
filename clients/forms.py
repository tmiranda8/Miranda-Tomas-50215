from django import forms
from clients import models
class NewClient(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ('first_name', 'last_name', 'birthday', 'phone', 'email')

    def __init__(self, *args, **kwargs):
        super(NewClient, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['id'] = 'fist_name'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['id'] = 'last_name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['birthday'].widget.attrs['class'] = 'form-control'
        self.fields['birthday'].widget.attrs['id'] = 'birthday'
        self.fields['birthday'].widget.attrs['placeholder'] = 'Fecha de nacimiento'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['id'] = 'phone'
        self.fields['phone'].widget.attrs['placeholder'] = 'Telefono'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electronico'
        # self.fields[''].widget.attrs['class'] = ''
        # self.fields[''].widget.attrs['id'] = ''
        # self.fields[''].widget.attrs['placeholder'] = ''
        # self.fields[''].widget.attrs['class'] = ''
        # self.fields[''].widget.attrs['id'] = ''
        # self.fields[''].widget.attrs['placeholder'] = ''