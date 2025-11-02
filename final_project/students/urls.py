from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("students/", views.students_list, name="list"),
    path("students/<int:pk>/", views.student_detail, name="detail"),
    path("students/create/", views.student_create, name="create"),
    path("students/<int:pk>/edit/", views.student_update, name="update"),
    path("students/<int:pk>/delete/", views.student_delete, name="delete"),
]
