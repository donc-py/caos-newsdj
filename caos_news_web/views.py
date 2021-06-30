from django.shortcuts import render
from. forms import LoginForm, NewsForm, RegisterForm
import requests
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.contrib import messages
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login, logout, authenticate
from .serializers import UserSerializer, RegisterSerializer, NewsSerializer, UserSerializer2
from rest_framework import status
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# API
class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        res = logout(request)
        print(res)
        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
    def get(self, request):
        # Borramos de la request la información de sesión
        res = logout(request)
        print(res)
        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

class LoginAPI(APIView):

    def post(self, request):
        #serializer = AuthTokenSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #user = serializer.validated_data['user']

        user = authenticate(email=request.data['email'], password=request.data['password'])

        print(user)
        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            
            return Response({
        "user":  UserSerializer2(user).data
        })

        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)

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
    
    return render(request, 'home.html', {'user':{}})
def afptercer10(request):
    return render(request, 'afptercer10.html', {})
@login_required    
def periodista(request):
    return render(request, 'periodista.html', {})

@login_required    
def adminv(request):
    return render(request, 'admin.html', {})

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
            
            post_data = {'username': form.cleaned_data['Correo'],'email': form.cleaned_data['Correo'], 'password': form.cleaned_data['Clave']}
            user = authenticate(email=form.cleaned_data['Correo'], password=form.cleaned_data['Clave'])
            if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("/periodista")
            
            #response = requests.post('http://127.0.0.1:8000/api/loginapi/', data=post_data)
            #print(response.json())
            #request.session['user'] = response.json()['user']          
            #login(request, response)
            #login(request, user)
            #print(request.user)
            #return HttpResponseRedirect("/")
            #return render(request, 'home.html', {'user': response.json()['user']})
    
    else:
        form = LoginForm()   
    context = {'form': form}
    return render(request, 'ingreso.html', context)

def registro(request):

    if request.method == 'POST':
        #username = request.POST.get('username', '')
        #password = request.POST.get('password', '')
        #print(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            post_data = {'username':form.cleaned_data['Usuario'],'email': form.cleaned_data['Correo'], 'password': form.cleaned_data['Clave']}
            response = requests.post('http://127.0.0.1:8000/api/registerapi/', data=post_data)
            print(response.text)
            messages.success(request, "Usuario registrado satisfactoriamente")
            return render(request, 'registro.html', {})
    
    else:
        form = RegisterForm()   
    context = {'form': form}
    return render(request, 'registro.html', context)
    
@login_required
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
@login_required    
def logoutv(request):
    if request.method == 'POST':


        res = logout(request)
        return render(request, 'ingreso.html')

def vacunarusa(request):
    return render(request, 'vacunarusa.html', {})
