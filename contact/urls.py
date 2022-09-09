from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('view_contacts/', views.view_contacts, name='view_contacts'),
]
