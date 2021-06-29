from django.shortcuts import render
from. forms import LoginForm, NewsForm
import requests
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, NewsSerializer
# Create your views here.

# API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
class NewsRegisterAPI(generics.GenericAPIView):
    serializer_class = NewsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "Response": "Account Created"
        })

def home(request):
    return render(request, 'home.html', {})
def afptercer10(request):
    return render(request, 'afptercer10.html', {})
def periodista(request):
    return render(request, 'periodista.html', {})

def casotomas(request):
    return render(request, 'casotomas.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def ingreso(request):

    if request.method == 'POST':
        #username = request.POST.get('username', '')
        #password = request.POST.get('password', '')
        #print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            post_data = {'username':'usernsssss','email': form.cleaned_data['Correo'], 'password': form.cleaned_data['Clave']}
            response = requests.post('http://127.0.0.1:8000/api/registerapi/', data=post_data)
            print(response.text)
            return render(request, 'home.html', {})
    
    else:
        form = LoginForm()   
    context = {'form': form}
    return render(request, 'ingreso.html', context)

def registro(request):

    if request.method == 'POST':
        #username = request.POST.get('username', '')
        #password = request.POST.get('password', '')
        #print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            post_data = {'username':'usernsssss','email': form.cleaned_data['Correo'], 'password': form.cleaned_data['Clave']}
            response = requests.post('http://127.0.0.1:8000/api/registerapi/', data=post_data)
            print(response.text)
            return render(request, 'registro.html', {})
    
    else:
        form = LoginForm()   
    context = {'form': form}
    return render(request, 'registro.html', context)
def news(request):

    if request.method == 'POST':
        print(request.POST)
        form = NewsForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            post_data = {'nombre': form.cleaned_data['nombre'], 'noticia': form.cleaned_data['noticia'], 'email': form.cleaned_data['email'], 'documento': form.cleaned_data['documento'], 'pasaporte': form.cleaned_data['pasaporte'], 'telefono': form.cleaned_data['telefono'], 'ciudad': form.cleaned_data['ciudad']}
            response = requests.post('http://127.0.0.1:8000/api/newsregisterapi/', data=post_data)
            print(response.json)
            return render(request, 'home.html', {})
    
    else:
        form = NewsForm()   
    context = {'form2': form}
    return render(request, 'news.html', context)

def vacunarusa(request):
    return render(request, 'vacunarusa.html', {})
