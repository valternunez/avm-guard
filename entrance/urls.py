from django.urls import path
from .views import NonResidentCreateView

urlpatterns = [
    path('non_residents/', NonResidentCreateView.as_view(), name='non_resident_create'),
]