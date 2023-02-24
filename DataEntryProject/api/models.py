from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField


class HealthInstitution(models.Model):
    """
    Database table HealthInstitution definition
    """
    institution_name=models.CharField(max_length=250,unique=True,blank=False)
    email=models.EmailField(blank=False,unique=True)
    phone_number=PhoneNumberField(null=False,blank=False,unique=True)
    city = models.CharField(max_length=255,blank=False)
    location=PlainLocationField(based_fields=['city'], zoom=7)
    zipcode = models.CharField(max_length=10,blank=False)
    capacity=models.IntegerField(blank=False)
    attribute = models.JSONField(default={})

    class Meta:
        db_table='health_insitution'
        verbose_name = "health institution"
    
    def __str__(self):
        return  self.institution_name
    
class ProfessionalDetails(models.Model):
    """
    Database table Professional Details definition
    """
    name=models.CharField(max_length=250,unique=True,blank=False)
    speciality=models.CharField(max_length=250,unique=True,blank=False)
    years_of_experience=models.IntegerField(blank=False)
    phone_number=PhoneNumberField(null=False,blank=False,unique=True)
    email=models.EmailField(blank=False,unique=True)
    resume=models.FileField(blank=False,upload_to='uploads')
    class Meta:
        db_table='professional_details'
        verbose_name = "professional_detail"
        
    def __str__(self):
        return  self.name 
        
    
class EventDetails(models.Model):
    """
    Database table Event Details definition
    """
    event_title=models.CharField(max_length=250,unique=True,blank=False)
    event_date=models.DateTimeField(unique=True,blank=False)
    event_description = models.TextField(null=False)
    event_duration=models.PositiveIntegerField(null=False)
    event_guests=models.PositiveIntegerField(null=False)
    city = models.CharField(max_length=255,blank=False)
    location=PlainLocationField(based_fields=['city'], zoom=7)    
    class Meta:
        db_table='event_details'
        verbose_name = "event_detail"
        
    def __str__(self):
        return  self.event_title

    

    


    
