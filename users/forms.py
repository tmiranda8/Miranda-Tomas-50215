from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'user form-control form-control-user'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['id'] = 'password'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        
        self.fields['username'].label = 'Usuario'
        self.fields['password'].label = 'Contraseña'
    class Meta:
        model = User

class CreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id':'first_name','placeholder':'Nombre'}))
    last_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id':'last_name','placeholder':'Apellido'}))

    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password1'].widget.attrs['id'] = 'password1'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password2'].widget.attrs['id'] = 'password2'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repetir contraseña'
        
        self.fields['username'].label = 'Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Repetir contraseña'
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

class EditForm(UserChangeForm):
    password = None
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['first_name'].widget.attrs['id'] = 'first_name'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['last_name'].widget.attrs['id'] = 'last_name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        # self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        # self.fields['password'].widget.attrs['id'] = 'password'
        # self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electronico'
        self.fields['date_joined'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['date_joined'].widget.attrs['id'] = 'date_joined'
        
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['username'].label = 'Usuario'
        # self.fields['password'].label = 'Contraseña'
        self.fields['email'].label = 'Correo electronico'
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'date_joined')

class ResetPwForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'user form-control form-control-user'
        self.fields['old_password'].widget.attrs['id'] = 'old_password'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Contraseña actual'
        
        self.fields['new_password1'].widget.attrs['class'] = 'user form-control form-control-user'
        self.fields['new_password1'].widget.attrs['id'] = 'new_password1'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Nueva contraseña'
        
        self.fields['new_password2'].widget.attrs['class'] = 'user form-control form-control-user'
        self.fields['new_password2'].widget.attrs['id'] = 'new_password2'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirme la contraseña'