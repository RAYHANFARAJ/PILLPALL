from django.contrib import admin
from django.urls import path
from DSTRPJT import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Page d'accueil
    path('dashboard/', views.dashboard, name='dashboard'),  # Tableau de bord
    path('add-medicine/', views.add_medicine, name='add_medicine'),  # Ajouter un médicament
    path('medicine-list/', views.medicine_list, name='medicine_list'),  # Liste des médicaments
    path('dispense-medicine/', views.dispense_medicine, name='dispense_medicine'),  # Distribuer un médicament
    path('login/', views.login_view, name='login'),  # Vue pour la connexion
    path('signup/', views.signup_view, name='signup'),  # Vue pour l'inscription
    path('home_authenticated/', views.home_authenticated, name='home_authenticated'),

]
