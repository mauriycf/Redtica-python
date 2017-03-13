from django.db import models
from django.contrib import admin

from draceditor.widgets import AdminDraceditorWidget

from .models import Entrada,Categoria

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }
    prepopulated_fields = {'slug': ('titulo',)}
    list_display = ('titulo', 'active')
    list_editable = ('active', )
    search_fields = ('titulo', )

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('nombre',)}
	list_display = ('nombre', 'slug', 'active')
	list_editable = ('active', )
	search_fields = ('nombre', )

admin.site.register(Entrada, YourModelAdmin)

admin.site.register(Categoria, CategoryAdmin)