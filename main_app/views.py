from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    project = Project.objects.all()
    return render(request, 'project/index.html', {'project': project})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)

    context = {
    'project': project,
    }
    return render(request, 'project/detail.html', context)

# MAILCHIMP
