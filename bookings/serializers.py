from rest_framework import serializers
from .models import Organization, Space, Service, Booking, Payment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class SpaceSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    class Meta:
        model = Space
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    space = SpaceSerializer(read_only=True)
    class Meta:
        model = Service
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    space = SpaceSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = '__all__'
