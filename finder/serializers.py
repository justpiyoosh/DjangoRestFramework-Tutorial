from finder.models import Casino
from rest_framework import serializers

class CasinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = '__all__'