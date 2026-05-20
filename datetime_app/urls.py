from django.urls import path
from . import views

urlpatterns = [
    # Route the root URL to our dynamic calculator view
    path('', views.time_calculator_view, name='time_calculator_view'),
]
