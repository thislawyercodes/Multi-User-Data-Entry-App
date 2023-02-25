from django.test import TestCase
from ..models import HealthInstitution,ProfessionalDetails,EventDetails


class HealthInstitutionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        HealthInstitution.objects.create(      
        institution_name="NayuuYuRki Hospital",
        email="yyuEgmail@gmail.com",
        phone_number="+27798888098",
        city= "Nanyuki",
        location="456",
        zipcode= "30100",
        capacity=400,
        attribute={}
        )

    def test_health_institution_name(self):
        health_institution = HealthInstitution.objects.get(id=1)
        field_label = health_institution._meta.get_field("institution_name").verbose_name
        self.assertEqual(field_label,"institution name")

    def test_name_max_length(self):
        health_institution = HealthInstitution.objects.get(id=1)
        max_length = health_institution._meta.get_field("institution_name").max_length
        self.assertEqual(max_length, 250)


class ProfessionDetailsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ProfessionalDetails.objects.create(
        name= "Dr Muthee",
        speciality="Children care",
        years_of_experience= 2,
        phone_number="+254741999245",
        email="akalerupe@gmail.com",
        resume="http://127.0.0.1:8000/uploads/Screenshot_from_2023-02-22_12-54-31.png"
        )

    def test_professional_details_label(self):
        profession = ProfessionalDetails.objects.get(id=1)
        field_label = profession._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        profession = ProfessionalDetails.objects.get(id=1)
        max_length = profession._meta.get_field("name").max_length
        self.assertEqual(max_length, 250)

class EventDetailsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        EventDetails.objects.create(
        event_title="Matter Heart Run",
        event_date="2023-02-14T11:58:06Z",
        event_description="Annual matter heart run cancer day event",
        event_duration= 2,
        event_guests=200,
        city="Nairobi",
        location="-0.003089904783662708,0.011844635009765625"
        )

    def test_event_label(self):
        event = EventDetails.objects.get(id=1)
        field_label = event._meta.get_field("event_title").verbose_name
        self.assertEqual(field_label, "event title")

    def test_event_name_max_length(self):
        event = EventDetails.objects.get(id=1)
        max_length = event._meta.get_field("event_title").max_length
        self.assertEqual(max_length, 250)