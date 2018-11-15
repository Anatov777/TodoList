from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            allTasks = Task.objects.all()
            messages.success(request, ('Задача была добавлена в список!'))
            return render(request, 'App_ToDoList/homePage.html', {'allTasks': allTasks})

    else:
        allTasks = Task.objects.all()
        return render(request, 'App_ToDoList/homePage.html', {'allTasks': allTasks})

    messages.success(request, ('Введите задачу! (не более 250 символов)'))
    return redirect('home')

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ('Задача была удалена.'))
    return redirect('home')

def cross_off(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('home')

def uncross(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = False
    task.save()
    return redirect('home')

def edit(request, task_id):
    if request.GET.get('editTextString'):
        task = Task.objects.get(pk=task_id)
        editData = request.GET.get('editTextString', None)
        task.textString = editData
        task.save()
        messages.success(request, ('Задача была изменена!'))
        return redirect('home')
    else:
        return redirect('home')
