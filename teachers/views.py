from django.shortcuts import render, redirect

from .forms import TeacherForm
from .models import Teacher


def home(request):
    """Home page."""
    return render(request, "home.html", {"title": "Home"})


def teacher_create(request):
    """Teacher page."""
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_teachers_list")
    else:
        form = TeacherForm()
    return render(request, "teacher.html", {"title": "Teacher", "form": form})


def get_teachers_list(request):
    """Get all teachers."""
    teachers = Teacher.objects.all().values()
    return render(
        request, "all_teachers.html", {"teachers": teachers, "title": "All Teachers"}
    )
