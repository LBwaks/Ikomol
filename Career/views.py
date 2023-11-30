from django.shortcuts import render
from .models import Job
from django.views.generic import ListView, DetailView

# Create your views here.


class CareerListView(ListView):
    model = Job
    template_name = "jobs/jobs.html"

    def get_queryset(self):
        return super().get_queryset()


class CareerDetailView(DetailView):
    model = Job
    template_name = "jobs/job-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job"] = self.get_object()
        return context
