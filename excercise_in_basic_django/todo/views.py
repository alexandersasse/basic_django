from django.shortcuts import render, HttpResponse
from django.urls import reverse
from .models import todos

# Create your views here.

def home(request):
    return HttpResponse(f"<h2>Todo</h2>")

def position(request, position):
    ### Retrieving data from models.py
    data_from_todo_in_models = todos[position - 1]
    ### Building up the data for display
    title = f"<h2>{data_from_todo_in_models['topic']}</h2>"
    entry = f"<h3>{data_from_todo_in_models['text']}</h3>"
    status = f"<h3>Status: {data_from_todo_in_models['status'].upper()}</h3>"
    home = f"<a href='{reverse('todo')}'>| Home |</a>"
    backwards = f"<a href='{reverse('todo-position', args=[position - 1])}'>Previous entry</a>"
    forwards = f"<a href='{reverse('todo-position', args=[position + 1])}'>Next entry</a>"
    ### Keep navigation in range
    if position == 1: backwards = "Previous entry"
    if position == len(todos): forwards = "Next entry"
    ### Putting it together & return
    content = f"{title}{entry}{status}{backwards}{home}{forwards}"
    return HttpResponse(content)
