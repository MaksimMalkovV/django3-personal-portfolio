from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects':projects})

def skils(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/skils.html', {'projects':projects})