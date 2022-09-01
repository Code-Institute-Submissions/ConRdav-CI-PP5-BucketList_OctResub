from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_testimonials, name='view_testimonials'),
]
