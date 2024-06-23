from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=100)
    policy = models.TextField()

class Space(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    maximum_capacity = models.IntegerField()
    opening_hours = models.CharField(max_length=100)
    facilities = models.TextField()

class Service(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    additional_cost = models.DecimalField(max_digits=6, decimal_places=2)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE, null=True, blank=True)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=50)  # e.g., pending, confirmed, paid, cancelled
    notes = models.TextField(blank=True, null=True)

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)  # e.g., credit card, bank transfer, etc.
    payment_status = models.CharField(max_length=50)  # e.g., paid, pending, refunded
