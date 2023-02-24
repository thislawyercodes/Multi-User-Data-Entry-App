from django.urls import path
from .views import HealthInstitutionList,ProfessionalDetail,EventDetail,HealthInstitutionDetail,ProfessionalDetailList,EventDetailList

app_name='api'

urlpatterns=[
    path('healthinstitution/',HealthInstitutionList.as_view(),name='health_institution_list'),
    path('healthinstitution/<int:pk>/',HealthInstitutionDetail.as_view(),name='health_institution_detail'),
    path('professionalDetail/',ProfessionalDetailList.as_view(),name='professional_detail_list'),
    path('professionalDetail/<int:pk>/',ProfessionalDetail.as_view(),name='professional_detail'),
    path('eventDetail/',EventDetailList.as_view(),name='event__list'),
    path('eventDetail/<int:pk>/',EventDetail.as_view(),name='event__detail')
]