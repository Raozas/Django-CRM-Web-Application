from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Student
from .forms import StudentForm

@login_required
def dashboard(request):  # can be your “students” landing page
    return redirect("students:list")

@login_required
def students_list(request):
    qs = Student.objects.all()
    q_group = request.GET.get("group", "").strip()
    q_sid = request.GET.get("student_id", "").strip()

    if q_group:
        qs = qs.filter(group__iexact=q_group)
    if q_sid:
        qs = qs.filter(student_id__iexact=q_sid)

    paginator = Paginator(qs, 20)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    ctx = {"page_obj": page_obj, "q_group": q_group, "q_sid": q_sid}
    return render(request, "students/list.html", ctx)

@login_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student created.")
        return redirect("students:list")
    return render(request, "students/form.html", {"form": form, "mode": "create"})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student updated.")
        return redirect("students:list")
    return render(request, "students/form.html", {"form": form, "mode": "update", "student": student})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.info(request, "Student deleted.")
        return redirect("students:list")
    return render(request, "students/confirm_delete.html", {"student": student})


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/profile.html", {"student": student})
