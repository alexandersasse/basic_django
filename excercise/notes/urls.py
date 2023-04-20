from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="notes"),
    path("sections/", views.sections, name="sections"),
    path("sections/<str:text_passed>", views.slug_query),
    path("<int:position>", views.position_query, name="notes-position"),
]