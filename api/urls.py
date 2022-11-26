from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view
urlpatterns = [
    path('schema', get_schema_view(title='API Schema', description='Guide for the Rest API'), name='schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'schema'}
    ), name='docs')
]
