from django.contrib import admin
from .models import user, Activity_period


# Register your models here.
admin.site.register(Activity_period)
admin.site.register(user)