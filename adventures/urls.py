from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_adventures, name='adventures'),
    path('<adventure_id>/', views.adventure_detail, name='adventure_detail'),
    path('excursions/<country>/', views.excursion_detail,
         name='excursion_detail'),
]
