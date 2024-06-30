from django.urls import path
from .views import contact

from . import views

urlpatterns = [
    path('protected', contact, name='contact_views'),
    path('contact', views.contact, name='contact'),

]
