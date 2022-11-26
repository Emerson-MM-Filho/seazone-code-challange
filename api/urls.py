from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from propriety import views as propriety_views
from booking import views as booking_views
from advertisement import views as advertisement_views

router = routers.DefaultRouter()
router.register(r'propriety', propriety_views.ProprietyViewSet, basename='propriety')
router.register(r'booking', booking_views.BookingViewSet, basename='booking')
router.register(r'advertisement', advertisement_views.AdvertisementViewSet, basename='advertisement')

urlpatterns = [
    path('', include(router.urls)),
    path('schema', get_schema_view(title='API Schema', description='Guide for the Rest API'), name='schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'schema'}
    ), name='docs')
]
