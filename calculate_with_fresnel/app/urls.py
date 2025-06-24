from django.urls import path

from app.views import (
    HomeView,
    CalculateView,
)

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('calculate/', CalculateView.as_view(), name='calculate'),
]