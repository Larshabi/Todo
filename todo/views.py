from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages

def TodoList(request):
    list = Todo.objects.all().order_by('-created_on')
    if request.method == "POST":
        title = request.POST.get('title')
        details = request.POST.get('detail')
        todo = Todo.objects.create(
            title=title,
            details = details,
        )
        todo.save()
    context = {'list': list}
    return render(request, 'todo/index.html', context)

def delete(request, t_id):
    item = Todo.objects.get(id = t_id)
    item.delete()
    messages.info(request, 'item removed!!!')    
    return redirect('index')
