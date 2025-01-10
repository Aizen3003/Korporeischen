"""
URL configuration for Korporeischen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Korporeischen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.glaw_stran, name="glawstran"),
    path("rabotniki/", views.stran_so_wsemi_rabami, name="stransowsemirabami"),
    path("rabotnik/<int:id>", views.lich_dan_rabotnika, name="lichdanrabotnika"),
    path("event_form/", views.dobaw_event, name="dobawevent"),
    path("swas_form/", views.swas_team_event, name="swasteamevent"),
    path("eventi/", views.stran_so_wsemi_eventomi, name="stransowsemieventomi"),
    path("eventi/<int:id>", views.dan_eventa, name="daneventa")
]
