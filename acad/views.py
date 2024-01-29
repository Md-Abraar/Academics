import json
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage
from acad.models import *
from django.db.models import Q
from django.utils.safestring import SafeString

# Create your views here.
def student(request):
    context = {
        'detained':False,
        'update': False
    }
    scheme_data = Schemes.objects.values_list('scheme', flat=True)
    scheme_data={'scheme_data':scheme_data}
    # print(scheme_data)    
    con={**context, **scheme_data}
    return render(request, "comprehensive.html", con)

def generate_rolls(request):
    context = {
        'update':False
    }
    if Comprehensive.objects.exists():
        context = {
            'update':True
        }
        
    return render(request, "comprehensive.html", context)


def inactive(request):
    return render(request, "inactive.html")


def detention(request):
    return render(request, "detention.html")


def student_mapping(request):
    if request.method=='POST':
        pscheme = request.POST.get('scheme')
        pbranch = request.POST.get('branch')
        psemester = request.POST.get('semester')

        try:
            students = Comprehensive.objects.filter(scheme=pscheme,branch=pbranch,semester=psemester,is_active=True)
            default_students = students.filter(is_detained=False,is_gap=False)
            other_students = students.filter(Q(is_detained=True) | Q(is_gap=False))
        except Comprehensive.DoesNotExist:
            print('Not found') #replace with actual handling  
    scheme_data = get_scheme_data()
    context = {'scheme_data': SafeString(scheme_data)}
    print(context) 
     
    return render(request, "student_mapping.html", context )


def faculty_mapping(request):
    scheme_data = get_scheme_data()
    context = {'scheme_data': SafeString(scheme_data)}
    print(context) 

    return render(request, "faculty_mapping.html", context)

def get_scheme_data():
    schemes = Schemes.objects.all()
    
    data_list = []
    for scheme in schemes:
        
        branch_list = scheme.branches.split()

        scheme_data = {
            'scheme': scheme.scheme,
            'branches': branch_list,
        }

        data_list.append(scheme_data)

    return data_list

def subject(request):
    if request.method=='POST':
        course_code=request.POST.get('course_code')
        subject=request.POST.get('subject')
        category=request.POST.get('category')
        scheme=request.POST.get('scheme')
        semester=request.POST.get('semester')
        mode=request.POST.get('mode')
        credits=request.POST.get('credits')
        type1=request.POST.get('type')
        end_exam_marks=request.POST.get('end_exam_marks')
        cia_marks=request.POST.get('cia_marks')
        total_marks=request.POST.get('total_marks')
        branch = request.POST.getlist('branch')
        
        mem=Subjects(course_code = course_code, subject = subject, category = category, scheme = scheme,
                      semester = semester, mode = mode,credits = credits,type = type1, end_exam_marks = end_exam_marks,
                    cia_marks = cia_marks, total_marks = total_marks)
        mem.save()    
        print(branch)

        for i in branch:
            bran = Branch(branch = i, course_code = course_code)
            bran.save()
        return redirect('show')
    # scheme_data = Schemes.objects.values('scheme')

    # scheme_data = Schemes.objects.all()
    # scheme_list = scheme_data.values_list('scheme', flat=True)
    scheme_data = get_scheme_data()
    context = {'scheme_data': scheme_data}
    print(scheme_data)
    return render(request, "subj.html", {'scheme_data':SafeString(scheme_data)})


def marks(request):
    return render(request, "marks.html")


def show(request):
    scheme_filter = request.GET.get('scheme', '')
    sem_filter = request.GET.get('semester', '')
    type_filter = request.GET.get('type', '')  
    search_query = request.GET.get('search', '')
    # Retrieve subject records
    all_records = Subjects.objects.all().order_by('-id')
    if scheme_filter:
        all_records = all_records.filter(scheme=scheme_filter)
    if sem_filter:
        all_records = all_records.filter(semester=sem_filter)
    if type_filter:
        all_records = all_records.filter(type=type_filter)

    subjects_records = all_records.filter(subject__contains=search_query).order_by('-id')
    
    # Iterate through subject records and fetch associated branches
    subjects_with_branches = []
    for subject_record in subjects_records:
        # Assuming you have a ForeignKey named 'course' in Subjects model
        course_code = subject_record.course_code
        branches = Branch.objects.filter(course_code=course_code).values_list('branch', flat=True)
        subjects_with_branches.append({'subject': subject_record, 'branches': branches})

    # Paginate the combined list
    page = request.GET.get('page', 1)
    records_per_page = 4
    paginator = Paginator(subjects_with_branches, records_per_page)
    
    try:
        records = paginator.page(page)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    
    context = {
        'records':records,
        'search_query':search_query,
        'scheme_filter':scheme_filter,
        'sem_filter':sem_filter,
        'type_filter':type_filter
    }
    return render(request, 'show.html', context)


@require_POST
def delete_record(request, record_id):
    # Handle record deletion
    branches = Branch.objects.filter(course_code=Subjects.objects.get(id=record_id).course_code)
    branches.delete()
    record = get_object_or_404(Subjects, id=record_id)
    record.delete()
    # return JsonResponse({'success': True})
    return redirect("show")
    
def edit_record(request, record_id):
    # record = get_object_or_404(Subjects, id=record_id)
    course_code=request.POST.get('course_code')
    subject=request.POST.get('subject')
    category=request.POST.get('category')
    scheme=request.POST.get('scheme')
    semester=request.POST.get('semester')
    mode=request.POST.get('mode')
    type1=request.POST.get('type')
    credits=request.POST.get('credits')
    end_exam_marks=request.POST.get('end_exam_marks')
    cia_marks=request.POST.get('cia_marks')
    total_marks=request.POST.get('total_marks')
    branch = request.POST.getlist('branch')
    
    mem=Subjects.objects.get(id=record_id)
    
    mem.course_code=course_code
    mem.subject=subject
    mem.category=category
    mem.scheme=scheme
    mem.semester=semester
    mem.mode=mode
    mem.type=type1
    mem.credits=credits
    mem.end_exam_marks=end_exam_marks
    mem.cia_marks=cia_marks
    mem.total_marks=total_marks
    mem.save()

    #Delete already present entries and update with new ones
    Branch.objects.filter(course_code=course_code).delete()

    for i in branch:
        bran = Branch(branch = i, course_code = course_code)
        bran.save()
        
    return redirect("show")

def enter(request):
    return render(request, 'entermarks.html')

