from django.db import models
from django.contrib import admin

from draceditor.widgets import AdminDraceditorWidget
from ckeditor.widgets import CKEditorWidget

from .models import Entrada,Categoria,Color

class YourModelAdmin(admin.ModelAdmin):
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
admin.site.register(Color)