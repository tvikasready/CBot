from .models import Synonym
from rest_framework import serializers

class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = ('word',)


