from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"
