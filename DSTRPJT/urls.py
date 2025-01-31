from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route pour la page d'accueil
    path('home_authenticated/', views.home_authenticated, name='home_authenticated'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('notes/', views.notes, name='notes'),
    path('medicine-list/', views.medicine_list, name='medicine_list'),
    path('dispense_medicine/', views.dispense_medicine, name='dispense_medicine'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('etat-eau/', views.etat_eau, name='etat_eau'),
    path('test/', views.test_view, name='test'),
]
