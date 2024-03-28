from rest_framework import serializers
from .models import UserMember

class UserMemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMember
        fields = ['first_name', 'last_name', 'id_number', 'phone_number', 'email', 'voice_recording']


class UserMemberDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMember
        fields = '__all__'

