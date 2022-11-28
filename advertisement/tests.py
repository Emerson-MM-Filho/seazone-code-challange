from rest_framework import status
from rest_framework.test import APITestCase
from advertisement.models import Advertisement
from advertisement.serializers import AdvertisementSerializer


class TestAdvertisement(APITestCase):
    url = "/advertisement/"

    fixtures = ["initial_data.json"]

    def test_get_advertisement_api(self):
        response = self.client.get(self.url)
        expected_result = [AdvertisementSerializer(advertisement).data for advertisement in Advertisement.objects.active()]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data["results"], expected_result)

    def test_delete_advertisement_api(self):
        advertisement = Advertisement.objects.first()
        response = self.client.delete(f"{self.url}{advertisement.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_advertisement_instance(self):
        advertisement = Advertisement.objects.first()
        advertisement.delete()

        self.assertEqual(advertisement.active, False)
