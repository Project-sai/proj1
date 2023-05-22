from django.urls import path
from Gate_config import views


urlpatterns = [
    path('collect_data/',views.collect_data),
    path('gate_configurations/',views.gate_configurations,name="gate_configuration"),
    path('site_data/',views.site_data),
    path('live/',views.live),
]