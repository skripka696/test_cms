from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BootstrapStyleForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BootstrapStyleForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserLoginForm(BootstrapStyleForm, AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)


class UserRegistrForm(BootstrapStyleForm, UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'role', 'gender')

    def __init__(self, *args, **kwargs):
        super(UserRegistrForm, self).__init__(*args, **kwargs)
