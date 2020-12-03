from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 100)

	class Meta:
		verbose_name = ('Category')
		verbose_name_plural = ('Categories')

	def __str__(self):
		return self.name

class Todo(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField(blank = True)
	created = models.DateField(default = timezone.now().strftime("%d-%m-%Y"))
	due_date = models.DateField(default = timezone.now().strftime("%d-%m-%Y"))
	category = models.ForeignKey(Category, default = "general", on_delete = models.CASCADE)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.title