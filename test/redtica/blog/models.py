from django.db import models
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField("Nombre", max_length=255)
	slug = models.SlugField("Slug", max_length=255)
	active = models.BooleanField("Activo", default=True)
	created_at = models.DateTimeField("Creado el", auto_now_add=True)
	updated_at = models.DateTimeField("Actualizado el", auto_now=True)

	class Meta:
		verbose_name='Categoría'
		verbose_name_plural = 'Categorías'
		ordering = ['-created_at']

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Categoria, self).save(*args, **kwargs)

class Color(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre


class Entrada(models.Model):
	titulo = models.CharField(max_length=300)
	slug = models.SlugField("Slug", max_length=255)
	contenido = RichTextField(
			'Contenido',
			help_text='Contenido de la página',
			blank=True
		)
	etiqueta = models.ForeignKey(Categoria)
	colores = models.ForeignKey(Color)
	active = models.BooleanField("Activo", default=True)
	created_at = models.DateTimeField("Creado el", auto_now_add=True)
	updated_at = models.DateTimeField("Actualizado el", auto_now=True)

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Entrada, self).save(*args, **kwargs)

	class Meta:
		verbose_name='Entrada'
		verbose_name_plural = 'Entradas'
		ordering = ['-created_at']

