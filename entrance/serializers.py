from rest_framework import serializers
from .models import NonResident


class NonResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonResident
        fields = '__all__'
