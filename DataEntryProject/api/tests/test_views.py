from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

CREATE_HEALTH_INSTITUTION_URL = reverse('api:health_institution_list')
LIST_HEALTH_INSTITUTION_URL = reverse('api:health_institution_list')


class HealthInstitutionDetailTest(TestCase):    
    def test_details(self):
        health_institution ={
        "id": 13,
        "institution_name": "Erupe National Hopital",
        "email": "akrupe@gmail.com",
        "phone_number": "+254789999245",
        "city": "Nairobi",
        "location": "0.0008583068847324188,-0.01064300537109375",
        "zipcode": "30100",
        "capacity": 400,
        "attribute": {
            "type": "string"
        }
    }
        response = self.client.get(CREATE_HEALTH_INSTITUTION_URL, health_institution)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class HealthInstitutionListTest(APITestCase):
    def test_details(self):
        response = self.client.get(LIST_HEALTH_INSTITUTION_URL,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code,status.HTTP_200_OK)