from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_adventures, name='adventures'),
    path('<int:adventure_id>/', views.adventure_detail,
         name='adventure_detail'),
    path('excursions/<str:country>/', views.excursion_detail,
         name='excursion_detail'),
    path('add/', views.add_adventure, name='add_adventure'),
    path('edit/<int:adventure_id>/', views.edit_adventure, name='edit_adventure'),
]
