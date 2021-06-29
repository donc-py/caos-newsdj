from django import forms

class LoginForm(forms.Form):
    Correo = forms.EmailField(label='Correo', max_length=50)
    Clave = forms.CharField(label='Clave', widget=forms.PasswordInput())

class NewsForm(forms.Form):
    Titulo = forms.CharField(label='Titulo', max_length=50)
    Descripcion = forms.CharField(label='Descripcion',widget=forms.Textarea)
