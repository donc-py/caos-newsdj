"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import RegisterAPI, NewsRegisterAPI, LoginAPI,LogoutView
from knox import views as knox_views
urlpatterns = [
    path('', views.home, name="home"),
    path('contacto', views.contacto, name='contacto'),
    path('afptercer10', views.afptercer10, name='afptercer10'),
    path('periodista', views.periodista, name='periodista'),
    path('adminv', views.adminv, name='adminv'),
    path('ingreso', views.ingreso, name='ingreso'),
    path('logoutv', views.logoutv, name='logoutv'),
    path('registro', views.registro, name='registro'),
    path('news', views.news, name='news'),
    path('casotomas', views.casotomas, name='casotomas'),
    path('vacunarusa', views.vacunarusa, name='vacunarusa'),
    path('api/registerapi/', RegisterAPI.as_view(), name='registerapi'),
    path('api/loginapi/', LoginAPI.as_view(), name='loginapi'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/newsregisterapi/', NewsRegisterAPI.as_view(), name='newsregisterapi'),



]