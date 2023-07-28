from django.contrib import admin

from .models import *

admin.site.register(Driver)
admin.site.register(Passenger)
admin.site.register(Car)
admin.site.register(Station)
admin.site.register(Road)