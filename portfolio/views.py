from django.shortcuts import render
from .models import Project


def home(request):
    # get all projects
    projects = Project.objects.all()

    return render(request, "home.html", {"projects": projects})
