from django.shortcuts import render
from .models import TodoModel
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

# Create your views here.
class CreateTodo(CreateView):
    model = TodoModel
    fields = ['title', 'contents', 'completed']
    template_name = 'todo/update.html'
    success_url = reverse_lazy('todo:list')

    
class ListTodo(ListView):
    model = TodoModel
    template_name = 'todo/list.html'
    context_object_name = 'todos'


class DeleteTodo(DeleteView):
    model = TodoModel
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo:list')
    
    
class UpdateTodo(UpdateView):
    model = TodoModel
    fields = ['title', 'contents', 'completed']
    template_name = 'todo/update.html'
    success_url = reverse_lazy('todo:list')
    
    
class DetailTodo(DetailView):
    model = TodoModel
    template_name = 'todo/detail.html'
    context_object_name = 'todo'