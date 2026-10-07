from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('v1/', views.app2v1, name='v1'),
    path('v2/', views.app2v2, name='v2'),
]