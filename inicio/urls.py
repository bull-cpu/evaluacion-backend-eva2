from django.urls import path
from . import views

app_name = "inicio"

urlpatterns = [
    path("", views.index, name="inicio"),
    path("gatos/", views.gatos, name="gatos"),
    path("baloncesto/", views.baloncesto, name="baloncesto"),
]