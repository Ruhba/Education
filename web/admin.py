from django.contrib import admin

from . models import Facilities,School,Teachers,Clients,Contact

# Register your models here.

admin.site.register(Facilities)

admin.site.register(School)

admin.site.register(Teachers)

admin.site.register(Clients)

admin.site.register(Contact)