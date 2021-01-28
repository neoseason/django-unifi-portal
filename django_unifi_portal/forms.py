from django import forms
from django.forms import ModelForm
from django.template import Template
from django.contrib.auth.forms import User
from django.contrib.auth.forms import AuthenticationForm

from material import Layout, Row, Fieldset
from . import form_mixin as forms

class UnifiLoginForm(AuthenticationForm):
    #ATTENZIONE: maschero la username con la email
    username = forms.EmailField(label="Email Address", required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    template = Template("""
    {% form %}
        {% part form.username prefix %}<i class="material-icons prefix">email</i>{% endpart %}
        {% part form.password prefix %}<i class="material-icons prefix">lock</i>{% endpart %}
    {% endform %}
    """)


    title = "Unifi Login"


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
