from django import forms

class ServerForm(forms.Form):
    server_type = forms.CharField(label='Server Type', max_length=100)
    ipaddress = forms.GenericIPAddressField(label='IPAddress', max_length=100)
    fqdn = forms.CharField(label='FQDN', max_length=100)
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)


class loginpage(forms.Form):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)