from rest_framework import serializers
from .models import user,Activity_period

class Activity_periodSerializers(serializers.ModelSerializer):

    class Meta:
        model=Activity_period
        fields='__all__'

class userSerializers(serializers.ModelSerializer):
    activity=Activity_periodSerializers(many=True,read_only=True)
    class Meta:
        model=user
        fields='__all__'
