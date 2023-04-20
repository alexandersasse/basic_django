from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="todo"),
    path("<int:position>", views.position, name="todo-position"),
]