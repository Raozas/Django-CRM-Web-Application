from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "last_name", "first_name", "group", "is_active")
    search_fields = ("student_id", "first_name", "last_name", "group")
    list_filter = ("group", "is_active")
