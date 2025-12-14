from django.contrib import admin

# Based on admin.py in helloworld/pittrain
from .models import Equipment, Checkout 

# Register your models here.
admin.site.register(Equipment)
admin.site.register(Checkout)