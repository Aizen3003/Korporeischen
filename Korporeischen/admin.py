from Korporeischen import models
from django.contrib import admin

admin.site.register(models.CustomUser)
admin.site.register(models.Event)
admin.site.register(models.Team)
admin.site.register(models.Employee)