from django.shortcuts import render, redirect
from .models import Category, Todo

# Create your views here.

def todoview(request):
	todoviews = Todo.objects.all()
	categories = Category.objects.all()

	if request.method == 'POST':

		if 'Task_Add' in request.POST:
			todo_title = request.POST['Description']
			date = str(request.POST['date'])
			category = request.POST['category_select']
			content = todo_title + '--' + date + '--' + category
			Todo = Todo(title = todo_title, due_date = date, category = Category.objects.get(name = category))
			Todo.save()
			return redirect('/')

		if 'Tast_Delete' in request.POST:
			checked_list = request.POST['checkedbox']

			for todo_id in checked_list:
				todo = Todo.objects.get(id = int(todo_id))
				todo.delete()

	return render(request, "templates/base.html", {"todos":todos, "categories":categories})