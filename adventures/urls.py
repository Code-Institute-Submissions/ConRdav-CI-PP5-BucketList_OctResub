from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_adventures, name='adventures'),
    path('<int:adventure_id>/', views.adventure_detail,
         name='adventure_detail'),
    path('excursions/<str:country>/', views.excursion_detail,
         name='excursion_detail'),
    path('add/', views.add_adventure, name='add_adventure'),
    path('edit/<int:adventure_id>/', views.edit_adventure,
         name='edit_adventure'),
    path('delete/<int:adventure_id>/', views.delete_adventure,
         name='delete_adventure'),
    path('add_excursion/', views.add_excursion, name='add_excursion'),
    path('delete_excursion/<str:country>/', views.delete_excursion,
         name='delete_excursion'),

]
