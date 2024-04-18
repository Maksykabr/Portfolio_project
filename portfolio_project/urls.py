from django.urls import path
from .views import GetHomePage

urlpatterns = [
    path('', GetHomePage.as_view(), name='home')
]