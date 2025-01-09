from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('create/', views.CreateTodo.as_view(), name='create'),
    path('', views.ListTodo.as_view(), name='list'),
    path('delete/<int:pk>/', views.DeleteTodo.as_view(), name='delete'),
    path('update/<int:pk>/', views.UpdateTodo.as_view(), name='update'),
    path('detail/<int:pk>/', views.DetailTodo.as_view(), name='detail'),
]