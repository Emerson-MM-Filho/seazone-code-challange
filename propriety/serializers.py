from rest_framework import serializers
from .models import Propriety


class ProprietySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Propriety
        fields = "__all__"
