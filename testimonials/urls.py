from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_testimonials, name='testimonials'),
    path('add_testimonial/', views.AddTestimonial.as_view(), name='add_testimonial'),
]
