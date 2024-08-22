from django.contrib import admin

from cakeapp import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Owner)
admin.site.register(models.Client)
admin.site.register(models.Cake)
admin.site.register(models.Category)