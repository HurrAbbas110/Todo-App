from django.contrib import admin
from .models import Category, Todo

# Register your models here.

@admin.register(Todo)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ["title", "created", "due_date"]

@admin.register(Category)
class TodoAdmin(admin.ModelAdmin):
	list_display = ("name",)