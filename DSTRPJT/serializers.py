from rest_framework import serializers
from .models import DSTRPJT

class DSTRPJTserialize(serializers.ModelSerializer):
    class Meta:
        model = DSTRPJT
        fields = '__all__'  # Inclut tous les champs du modèle
