from django.contrib import admin
from .models import *

admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Reservation)
admin.site.register(Inventory)