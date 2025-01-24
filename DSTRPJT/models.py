from django.db import models
from django.contrib.auth.models import AbstractUser

class DSTRPJT(models.Model):
    pill_taken = models.BooleanField(default=False)  # Indique si la pilule a été prise
    water_level = models.FloatField(null=True, blank=True)  # Niveau d'eau
    updated_at = models.DateTimeField(auto_now=True)  # Dernière mise à jour

    def __str__(self):
        return f"Pill taken: {self.pill_taken}, Water level: {self.water_level}"


class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)  # Champ personnalisé pour distinguer les utilisateurs

    # Gestion des relations pour éviter les conflits avec le modèle User par défaut
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )
