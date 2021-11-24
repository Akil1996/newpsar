from django.urls import path
from . import views
urlpatterns = [
    path('', views.psr_home, name="psrhome"),
]