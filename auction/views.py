from django.shortcuts import render
from .models import section, lot

# Create your views here.
def main(request):
    a = len(lot.objects.all())
    return render(request, 'index.html', {"a": a})

def catolog(request):
    departments = section.objects.all().order_by('name')
    return render(request, 'catologs.html', {"departments": departments})

def items(request, dep):
    departments = section.objects.get(id=dep)
    return render(request, 'department.html', {'dep': departments})