from django import forms

class LoginForm(forms.Form):
    Correo = forms.EmailField(label='Correo', max_length=50)
    Clave = forms.CharField(label='Clave', widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    Usuario = forms.CharField(label='Usuario', max_length=50)
    Correo = forms.EmailField(label='Correo', max_length=50)
    Clave = forms.CharField(label='Clave', widget=forms.PasswordInput())

class NewsForm(forms.Form):
    
    nombre = forms.CharField(label='nombre',max_length=150)
    noticia = forms.CharField(label='noticia',widget=forms.Textarea)
    email = forms.EmailField(label='email',max_length=50)
    documento = forms.CharField(label='documento',widget=forms.Select)    
    pasaporte = forms.CharField(label='pasaporte',max_length=50)
    telefono = forms.CharField(label='telefono',max_length=50)
    ciudad = forms.CharField(label='ciudad',max_length=50)
