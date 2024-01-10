from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage
from acad.models import *

# Create your views here.
def student(request):
    context = {
        'detained':False
    }
    return render(request, "comprehensive.html", context)

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
        subject=request.POST.get('subject')
        category=request.POST.get('category')
        scheme=request.POST.get('scheme')
        semester=request.POST.get('semester')
        type1=request.POST.get('type')
        credits=request.POST.get('credits')
        end_exam_marks=request.POST.get('end_exam_marks')
        cia_marks=request.POST.get('cia_marks')
        total_marks=request.POST.get('total_marks')
        
       
        mem=Subjects(course_code=course_code,subject=subject, category=category, scheme=scheme,
                      semester=semester, type=type1,credits=credits, end_exam_marks=end_exam_marks,
                    cia_marks=cia_marks, total_marks=total_marks)
        mem.save()

        # con = {'course_code':course_code,'subject':subject,'category':category,'scheme':scheme,
        #      'semester':semester,'type':type1,'credits':credits,'end_exam_marks':end_exam_marks,
        #      'cia_marks':cia_marks,'total_marks':total_marks}
        
        # records=Subjects.objects.all()
        # return render(request, 'show.html',{records:records})
        return redirect('show')
    
    return render(request, "subj.html")


def marks(request):
    return render(request, "marks.html")

def show(request):
    # Create dummy records
    # for i in range(1, 51):
    #     YourModel.objects.create(name=f"Record {i}", description=f"Description {i}")

    # Retrieve and paginate records
    records = Subjects.objects.all()
    page = request.GET.get('page', 1)
    records_per_page = 2
    paginator = Paginator(records, records_per_page)
    try:
        records = paginator.page(page)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    return render(request, 'show.html', {'records': records})

# def add_record(request):
#     return render(request, 'subj.html')

@require_POST
def delete_record(request, record_id):
    # Handle record deletion
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
    type1=request.POST.get('type')
    credits=request.POST.get('credits')
    end_exam_marks=request.POST.get('end_exam_marks')
    cia_marks=request.POST.get('cia_marks')
    total_marks=request.POST.get('total_marks')

    mem=Subjects.objects.get(id=record_id)
    
    mem.course_code=course_code
    mem.subject=subject
    mem.category=category
    mem.scheme=scheme
    mem.semester=semester
    mem.type1=type1
    mem.credits=credits
    mem.end_exam_marks=end_exam_marks
    mem.cia_marks=cia_marks
    mem.total_marks=total_marks
    mem.save()
    return redirect("show")




    # rec=Subjects.objects.get(id=record_id)
    # return render(request, "show.html", {'record':rec})
    # if request.method == 'POST':
    #     # Handle form submission for editing the record
    #     # ...

    #     return JsonResponse({'success': True})
    # return JsonResponse({'success': False})

