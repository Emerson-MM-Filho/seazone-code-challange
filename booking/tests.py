import datetime
from rest_framework import status, serializers
from rest_framework.test import APITestCase
from advertisement.models import Advertisement
from api.error_code import ErrorCode

from booking.models import Booking
from booking.serializers import BookingSerializer

class TestBooking(APITestCase):
    url = "/booking/"

    fixtures = ["initial_data.json"]

    def test_update_booking_instance(self):
        booking = Booking.objects.first()
        default_commentary = booking.commentary
        booking.commentary = "another random commentary"
        booking.save()

        self.assertEqual(Booking.objects.first().commentary, default_commentary)

    def test_get_bookings(self):
        response = self.client.get(self.url)
        expected_result = [BookingSerializer(booking).data for booking in Booking.objects.all()]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data["results"], expected_result)

    def test_post_bookings(self):
        data = {
            "check_in": "2023-01-25",
            "check_out": "2023-01-30",
            "price": 3150.0,
            "commentary": "Some commentary",
            "guests_count": 4,
            "advertisement": 1
        }
        response = self.client.post(self.url, data=data)

        expected_result = BookingSerializer(Booking.objects.last()).data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEquals(response.data, expected_result)

    def test_post_with_wrong_checkout_date(self):
        check_in = "2023-01-25"
        check_out = "2023-01-24"
        data = {
            "check_in": check_in,
            "check_out": check_out,
            "price": 3150.0,
            "commentary": "Some commentary",
            "guests_count": 4,
            "advertisement": 1
        }
        response = self.client.post(self.url, data=data)

        expected_result = {
            "check_out": {
                "message": f"The check-out ({check_out}) date must be later than the check-in ({check_in}) date",
                "code": str(ErrorCode.INVALID_FIELD.value)
            }
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response.data, dict)
        self.assertEquals(response.json(), expected_result)

    def test_post_with_wrong_guests_count(self):
        advertisement = Advertisement.objects.first()

        data = {
            "check_in": "2023-01-25",
            "check_out": "2023-01-30",
            "price": 3150.0,
            "commentary": "Some commentary",
            "guests_count": 8,
            "advertisement": advertisement.pk
        }
        response = self.client.post(self.url, data=data)

        expected_result = {
            "guests_count": {
                "message": f"The maximum number of guests is: {advertisement.propriety.guests_limit}",
                "code": str(ErrorCode.INVALID_FIELD.value)
            }
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response.data, dict)
        self.assertEquals(response.json(), expected_result)

    def test_post_with_more_than_one_error(self):
        advertisement = Advertisement.objects.first()

        check_in = "2023-01-25"
        check_out = "2023-01-24"
        data = {
            "check_in": check_in,
            "check_out": check_out,
            "price": 3150.0,
            "commentary": "Some commentary",
            "guests_count": 8,
            "advertisement": advertisement.pk
        }
        response = self.client.post(self.url, data=data)

        expected_result = {
            "check_out": {
                "message": f"The check-out ({check_out}) date must be later than the check-in ({check_in}) date",
                "code": str(ErrorCode.INVALID_FIELD.value)
            },
            "guests_count": {
                "message": f"The maximum number of guests is: {advertisement.propriety.guests_limit}",
                "code": str(ErrorCode.INVALID_FIELD.value)
            }
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response.data, dict)
        self.assertEquals(response.json(), expected_result)

    def test_fail_case_method_validate_check_out_date(self):
        check_in = datetime.date(year=2023, month=1, day=25)
        check_out = datetime.date(year=2023, month=1, day=24)

        expected_result = serializers.ValidationError(
            {"check_out": f"The check-out ({check_out}) date must be later than the check-in ({check_in}) date"},
            code=ErrorCode.INVALID_FIELD.value
        )

        with self.assertRaises(serializers.ValidationError) as execution:
            BookingSerializer()._validate_check_out_date(check_in, check_out)

        self.assertEquals(
            execution.exception.get_full_details(),
            expected_result.get_full_details()
        )

    def test_success_case_method_validate_check_out_date(self):
        check_in = datetime.date(year=2023, month=1, day=25)
        check_out = datetime.date(year=2023, month=1, day=26)

        try:
            BookingSerializer()._validate_check_out_date(check_in, check_out)
        except:
            self.fail("BookingSerializer._validate_check_out_date method failing with correct dates.")

    def test_fail_case_method_validate_guests_count(self):
        advertisement = Advertisement.objects.first()

        expected_result = serializers.ValidationError(
            {"guests_count": f"The maximum number of guests is: {advertisement.propriety.guests_limit}"},
            code=ErrorCode.INVALID_FIELD.value
        )

        guests_count = advertisement.propriety.guests_limit + 1
        with self.assertRaises(serializers.ValidationError) as execution:
            BookingSerializer()._validate_guests_count(guests_count, advertisement)

        self.assertEquals(
            execution.exception.get_full_details(),
            expected_result.get_full_details()
        )

    def test_success_case_method_validate_guests_count(self):
        advertisement = Advertisement.objects.first()
        guests_count = advertisement.propriety.guests_limit

        try:
            BookingSerializer()._validate_guests_count(guests_count, advertisement)
        except:
            self.fail("BookingSerializer._validate_guests_count method failing with correct guests count.")

    def test_fail_case_method_validate_available_date(self):
        booking = Booking.objects.first()

        check_in = booking.check_in
        check_out = booking.check_out

        expected_result = serializers.ValidationError(
            {"check_in/check_out": f"Property {booking.advertisement.propriety} is already booked for the indicated dates"},
            code=ErrorCode.INVALID_BOOKING_SCHEDULING.value
        )

        with self.assertRaises(serializers.ValidationError) as execution:
            BookingSerializer()._validate_available_date(check_in, check_out, booking.advertisement)

        self.assertEquals(
            execution.exception.get_full_details(),
            expected_result.get_full_details()
        )

    def test_success_case_method_validate_available_date(self):
        check_in = datetime.date(year=2022, month=12, day=1)
        check_out = datetime.date(year=2022, month=12, day=3)

        advertisement = Advertisement.objects.first()

        try:
            BookingSerializer()._validate_available_date(check_in, check_out, advertisement)
        except:
            self.fail("BookingSerializer._validate_available_date method failing with correct check in and check out date.")
