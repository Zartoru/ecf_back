from django.shortcuts import render
from ecf_bdd.models import SchoolYear, Project, User

# Create your views here.
def index(request):
    return render(request, 'data_access/index.html')

def schoolyears(request):
    school_years = SchoolYear.objects.all()
    sy_data = {'school_years': school_years}

    return render(request, 'data_access/schoolyears.html', sy_data)

def projects(request):
    projects = Project.objects.all()
    proj_data = {'projects': projects}

    return render(request, 'data_access/projects.html', proj_data)

def users(request):
    users = User.objects.all()
    user_data = {'users': users}

    return render(request, 'data_access/users.html', user_data)