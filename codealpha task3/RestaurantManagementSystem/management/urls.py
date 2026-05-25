from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', MenuListView.as_view()),
    path('tables/', TableListView.as_view()),
    path('orders/', OrderView.as_view()),
    path('reservations/', ReservationView.as_view()),
    path('inventory/', InventoryView.as_view()),
]