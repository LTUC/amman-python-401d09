from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Thing

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]

class ThingSerializer(serializers.ModelSerializer):
    # owner_name = UserSerializer()
    owner_name = serializers.CharField(source='owner', read_only=True)
    class Meta:
        model = Thing
        fields = '__all__'
