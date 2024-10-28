from django.contrib import admin
from app_1.models import Habitat

class AdminHabitat(admin.ModelAdmin):

    list_display = ['nombre','duracion_estancia','fecha_ingreso']

admin.site.register(Habitat,AdminHabitat)

# Register your models here.
