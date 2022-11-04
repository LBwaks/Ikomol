from unicodedata import name
from django.urls import path
from core.views import HomeView 
from .views import ContactView,HomeView ,PricingsView,ServicesView,AboutView
urlpatterns =[
    path('',HomeView.as_view(),name='home'),
    # path('',HomeView,name='home'),
    path('pricing/',PricingsView.as_view(),name='pricing'),
    path('services/',ServicesView.as_view(),name ='services'),
    path('about/',AboutView.as_view(),name ='about' ),
    path('contact/',ContactView.as_view(),name="contact"),
    # path('test',test,name='test')
]