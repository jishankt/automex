from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('debug/', views.debug_clients, name='debug_clients'),
]