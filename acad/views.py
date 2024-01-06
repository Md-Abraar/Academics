from django.shortcuts import render
from acad.models import *

# Create your views here.
def student(request):
    return render(request, "comprehensive.html")

def inactive(request):
    return render(request, "inactive.html")

def detention(request):
    return render(request, "detention.html")

def student_mapping(request):
    return render(request, "student_mapping.html")

def faculty_mapping(request):
    return render(request, "faculty_mapping.html")

def electives(request):
    return render(request, "electives.html")

def subject(request):
    return render(request, "subj.html")

def marks(request):
    return render(request, "marks.html")
