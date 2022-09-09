from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_testimonials, name='testimonials'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
    path('edit/<int:user_id>/', views.edit_testimonial,
         name='edit_testimonial'),
    path('delete/<int:user_id>/', views.delete_testimonial,
         name='delete_testionial'),
]
