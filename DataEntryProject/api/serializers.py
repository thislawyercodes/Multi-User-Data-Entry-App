from rest_framework import serializers
from .models import HealthInstitution,EventDetails,ProfessionalDetails

class HealthInstitutionSerializer(serializers.ModelSerializer):
    """
    model serializer for the HealthInstitution table
    """
    class Meta:
        model=HealthInstitution
        fields="__all__"
        
class EventDetailsSerializer(serializers.ModelSerializer):
    """
    model serializer for the EventDetails table
    """
    class Meta:
        model=EventDetails
        fields="__all__"

class ProfessionalDetailsSerializer(serializers.ModelSerializer):
    """
    model serializer for the ProfessionalDetails table
    """
    class Meta:
        model=ProfessionalDetails
        fields="__all__"
        

 