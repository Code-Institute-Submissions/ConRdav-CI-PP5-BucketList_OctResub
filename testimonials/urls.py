from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_testimonials, name='testimonials'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
]
