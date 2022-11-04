from django.test import TestCase
from .models import City
from django.urls import reverse


class CapitalTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Capital Cities")

    def test_capital_createview(self):
        response = self.client.post(
            reverse("capital_new"), {"city": "New Delhi", "country": "India"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(City.objects.last().city, "New Delhi")
        self.assertEqual(City.objects.last().country, "India")

    @classmethod
    def setUpTestData(cls):
        cls.city = City.objects.create(city="Riga", country="Latvia")

    def test_capital_city(self):
        self.assertEqual(self.city.city, "Riga")

    def test_capital_country(self):
        self.assertEqual(self.city.country, "Latvia")
