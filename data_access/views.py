from django.shortcuts import render
from ecf_bdd.models import SchoolYear

# Create your views here.
def index(request):
    return render(request, 'data_access/index.html')

def schoolyears(request):
    school_years = SchoolYear.objects.all()
    data = {'school_years': school_years}

    return render(request, 'data_access/schoolyears.html', data)