from django.db import models
from django.contrib import admin

from draceditor.widgets import AdminDraceditorWidget

from .models import Entrada
from .models import Categoria

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }

admin.site.register(Entrada, YourModelAdmin)

admin.site.register(Categoria)