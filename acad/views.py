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
    if request.method=='POST':
        course_code=request.POST.get('course_code')
        subject=request.POST.get('course_code')
        category=request.POST.get('category')
        scheme=request.POST.get('scheme')
        semester=request.POST.get('semester')
        type1=request.POST.get('type')
        credits=request.POST.get('credits')
        end_exam_marks=request.POST.get('end_exam_marks')
        cia_marks=request.POST.get('cia_marks')
        total_marks=request.POST.get('total_marks')
        
        
        con = {'course_code':course_code,'subject':subject,'category':category,'scheme':scheme,
             'semester':semester,'type':type1,'credits':credits,'end_exam_marks':end_exam_marks,
             'cia_marks':cia_marks,'total_marks':total_marks}
        
        # sub=Subjects.objects.all()
        return render(request, 'show.html',con)
    
    return render(request, "subj.html")

def show(request):
    return render(request, 'show.html')


def marks(request):
    return render(request, "marks.html")
