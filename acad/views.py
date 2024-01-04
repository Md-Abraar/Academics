from django.shortcuts import render
from acad.models import *

# Create your views here.
def index(request):
    return render(request, "subj.html")