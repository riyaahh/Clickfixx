from django.contrib import admin

# Register your models here.
from . models import service,appointments,provider,providerpaymentdetails 
admin.site.register(service)
admin.site.register(appointments)
admin.site.register(provider)
admin.site.register(providerpaymentdetails)
