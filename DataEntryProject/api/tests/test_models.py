import pytest

from api.models import HealthInstitution
from api.serializers import HealthInstitutionSerializer
from django.urls import reverse


@pytest.mark.django_db
def test_list_health_institutions(client):
    url = reverse('list-health_institutions')
    response = client.get(url)

    health_institution = HealthInstitution.objects.all()
    expected_data = HealthInstitutionSerializer(health_institution, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data