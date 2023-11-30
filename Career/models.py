from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.translation import gettext as _
from django_extensions.db.fields import AutoSlugField

# Create your models here.
JOB_TYPES = [
    ("Contract", "Contract"),
    ("Fultime", "Fultime"),
]


def my_slugify_function(content):
    return content.replace("_", "-").lower()


class Job(models.Model):
    """Model definition for Job."""

    # TODO: Define fields here
    user = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=50)
    slug = AutoSlugField(populate_from="title", slugify_function=my_slugify_function)
    job_type = models.CharField(_("Job Type"), choices=JOB_TYPES, max_length=50)
    location = models.CharField(_("Location"), max_length=50)
    summary = RichTextField()
    roles = RichTextField()
    skills = RichTextField()
    acedemic_qualification = RichTextField()
    experience = RichTextField()
    deadline = models.DateTimeField(_("Deadline"), auto_now=False, auto_now_add=False)
    created = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Job."""

        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        """Unicode representation of Job."""
        return self.title

    # def save(self):
    #     """Save method for Job."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for Job."""
        return reverse("career-details", kwargs={"slug": self.slug})

    # TODO: Define custom methods here
