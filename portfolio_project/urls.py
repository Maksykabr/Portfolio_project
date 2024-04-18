from django.urls import path
from .views import GetHomePage

app_name = 'portfolio'

urlpatterns = [
    path('', GetHomePage.as_view(), name='home')
]