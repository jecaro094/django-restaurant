# Create some views here
from django.shortcuts import render
from .models import Project

def project_static(request):
    context = {}
    return render(request, 'project_static.html', context)