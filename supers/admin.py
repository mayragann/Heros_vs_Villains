from django.contrib import admin
from super_types.models import SuperType
from .models import Super


# Register your models here.
admin.site.register(Super)
admin.site.register(SuperType)