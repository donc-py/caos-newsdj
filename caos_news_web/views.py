from django.shortcuts import render
from. forms import LoginForm
import requests
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
# Create your views here.

# Register API
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

def home(request):
    return render(request, 'home.html', {})

def casotomas(request):
    return render(request, 'casotomas.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def ingreso(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            post_data = {'email': form.cleaned_data['Correo'], 'password': form.cleaned_data['Clave']}
            response = requests.post('http://127.0.0.1:8000/api/registerapi/', data=post_data)
            print(response.json)
            return render(request, 'home.html', {})
    
    else:
        form = LoginForm()   
    context = {'form': form}
    return render(request, 'ingreso.html', context)

def vacunarusa(request):
    return render(request, 'vacunarusa.html', {})
