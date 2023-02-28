from django.urls import path

from . import views

# ? URLConfigurations
urlpatterns = [path("hello/", views.say_hello)]
