from django.contrib import admin
from contest import models

admin.site.register(models.ContestControl)
admin.site.register(models.Slave)
