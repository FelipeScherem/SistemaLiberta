from django.contrib import admin

# Register your models here.

from .models import bebida
admin.site.register(bebida)

from .models import comida
admin.site.register(comida)


