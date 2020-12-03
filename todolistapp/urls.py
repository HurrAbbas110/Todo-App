from django.urls import path
from . import views

app_name = 'todolistapp'

urlpatterns = [
	path('base/', views.todoview(), name = "todoview"),
]