"""
URL configuration for playground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from poll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('persons/', views.persons ),
    path('persons/persondetails/<int:id>/', views.persondetails),
    path('persons/persondetails/<int:id>/delete/', views.delete),
    path('persons/persondetails/<int:id>/updatepage/', views.updatepage),
    path('persons/persondetails/<int:id>/updatepage/updatepageprocess/', views.updatepageprocess),






    path('addpersonpage/', views.addpersonpage),
    path('addpersonpage/addpersonpageprocess/', views.addpersonpageprocess),



    path('test/', views.test),







]
