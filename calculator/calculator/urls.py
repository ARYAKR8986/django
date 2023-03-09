"""calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from operation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("addition/",views.AdditionView.as_view(),name="addition"),
    path("subtraction/",views.SubtractionView.as_view(), name="subtraction"),
    path("cube/",views.CubeView.as_view(), name="cube"),
    path("fact/",views.FactorialView.as_view(),name="fact"),
    path("armstrong/",views.Armstrong.as_view()),
    path("multiplication/",views.Multiplication.as_view()),
    path("prime/",views.Prime.as_view(),name="prime"),
    path("even/",views.Even.as_view(), name="even"),
    path("health/",views.Health.as_view(),name="health"),
    path("temp/",views.Temperature.as_view()),
    path("exponent/",views.Exponentview.as_view()),
    path("login/",views.Loginview.as_view()),
    path("registration/",views.Registrationview.as_view()),
    path("",views.HomeView.as_view(),name="home")
   



    
]
