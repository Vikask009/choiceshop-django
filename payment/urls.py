from django.urls import path
from . import views
urlpatterns = [
    #CHECK OUT PAYMENT:
    path('', views.checkout, name='checkout'),
    path('checkout/', views.checkout, name='checkout'),
]
