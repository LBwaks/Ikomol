from django.urls import path 
from .views import BlogsView,BlogDetailView,search
urlpatterns = [
    path('blogs/',BlogsView.as_view(),name='blogs'),
    path('blog-details/<slug>',BlogDetailView.as_view(),name="blog-details"),
    path('search/',search,name="search"),
]
