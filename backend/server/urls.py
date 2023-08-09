from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('services', views.services, name = 'services'),
    # path('ride-request/', views.ride_request, name='ride_request'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('trips', views.getTrips, name = 'trips'),
    path('ride-request', views.rideRequest, name = 'ride-request')

]
