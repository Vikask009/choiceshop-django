from django.urls import path
from . import views
urlpatterns = [
    #CHECK OUT PAYMENT:
    path('checkout/', views.checkout, name='checkout'),
]
