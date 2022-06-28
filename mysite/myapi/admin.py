from django.contrib import admin
from .models import Hero
from .models import Villian


# Register your models here.
# 3) if want to include in admin panel to crud/control import modelname from models.py(*above import) and register it here
admin.site.register(Hero)
admin.site.register(Villian)