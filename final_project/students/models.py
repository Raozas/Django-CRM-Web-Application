from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    group = models.CharField(max_length=32, db_index=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=True)
    joined_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["group", "student_id"]

    def __str__(self):
        return f"{self.student_id} - {self.last_name} {self.first_name}"
