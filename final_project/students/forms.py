from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["student_id", "first_name", "last_name", "group", "email", "phone",  "is_active"]
