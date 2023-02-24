from .models import HealthInstitution,ProfessionalDetails,EventDetails
from .serializers import HealthInstitutionSerializer,ProfessionalDetailsSerializer,EventDetailsSerializer
from rest_framework import permissions, generics
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

class CacheMixin(object):
    """_Base Redis Cache class
    """
    cache_timeout = 60
    def get_cache_timeout(self):
        return self.cache_timeout
    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)
              
class HealthInstitutionList(CacheMixin,generics.ListCreateAPIView):
    """
    Create or list all Health institutions
    """
    queryset=HealthInstitution.objects.all()
    serializer_class=HealthInstitutionSerializer
    permission_classes = [permissions.AllowAny]
    
class HealthInstitutionDetail(CacheMixin,generics.RetrieveUpdateDestroyAPIView):
    """
    Fetch,edit or delete a single health institution
    """
    queryset=HealthInstitution.objects.all()
    serializer_class=HealthInstitutionSerializer
    permission_classes = [permissions.AllowAny]     

class ProfessionalDetailList(CacheMixin,generics.ListCreateAPIView):
    """
    Create or list all Professional Details
    """
    queryset=ProfessionalDetails.objects.all()
    serializer_class=ProfessionalDetailsSerializer
    permission_classes = [permissions.AllowAny]     
  
class ProfessionalDetail(CacheMixin,generics.RetrieveUpdateDestroyAPIView):
    """
    Fetch,edit or delete Professional Details 
    one at a time
    """
    queryset=ProfessionalDetails.objects.all()
    serializer_class=ProfessionalDetailsSerializer
    permission_classes = [permissions.AllowAny]     

class EventDetailList(CacheMixin,generics.ListCreateAPIView):
    """
    Create or list all EventDetails
    """
    queryset=EventDetails.objects.all()
    serializer_class=EventDetailsSerializer
    permission_classes = [permissions.AllowAny]     

class EventDetail(CacheMixin,generics.RetrieveUpdateDestroyAPIView):
    """
    Fetch,edit or delete a single Event Detail
    """
    queryset=EventDetails.objects.all()
    serializer_class=EventDetailsSerializer
    permission_classes = [permissions.AllowAny]     


   
  

