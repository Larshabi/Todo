from django.urls import path
from todo import views

urlpatterns = [
    path('', views.TodoList, name="index"),
    path('del/<int:t_id>/', views.delete, name="del")
]
