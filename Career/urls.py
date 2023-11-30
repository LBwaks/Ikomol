from django.urls import path
from .views import CareerListView, CareerDetailView

urlpatterns = [
    path("", CareerListView.as_view(), name="careers"),
    path("career-details/<slug>", CareerDetailView.as_view(), name="career-details"),
]
