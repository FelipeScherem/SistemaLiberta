from django.contrib import admin

# Register your models here.

from .models import bebida
admin.site.register(bebida)

from .models import comida
admin.site.register(comida)

from .models import usuario
admin.site.register(usuario)
