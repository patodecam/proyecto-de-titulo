from django.urls import path
from .views import home,servicios

urlpatterns = [
    path('', home,name='home'),
    path('servicios', servicios,name='servicios'),
    
]
