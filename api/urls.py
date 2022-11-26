from django.urls import path, include
from rest_framework.schemas import get_schema_view
urlpatterns = [
    path('schema', get_schema_view(title='API Schema', description='Guide for the Rest API'), name='schema'),
]
