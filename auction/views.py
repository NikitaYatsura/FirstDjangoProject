from django.shortcuts import render
from .models import Section, Lot

# Create your views here.
def main(request):
    a = len(Lot.objects.all())
    return render(request, 'index.html', {"a": a})

def catolog(request):
    departments = Section.objects.all().order_by('name')
    return render(request, 'catologs.html', {"departments": departments})

def items(request, dep):
    departments = Section.objects.get(id=dep)
    return render(request, 'department.html', {'dep': departments})