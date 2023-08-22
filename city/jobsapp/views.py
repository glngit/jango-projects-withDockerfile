from django.shortcuts import render
from jobsapp.models import *

# Create your views here.
def index(request):
    return render(request,'jobsapp/index.html')

def hydjobsinfo(request):
    list_of_jobs=Hydjobs.objects.all()   # --or--   .order_by('date')
    dict={'jobs':list_of_jobs}
    return render(request,'jobsapp/hydjobs.html',context=dict)


def chennaijobsinfo(request):
    list_of_jobs=Chennaijobs.objects.all()   # --or--   .order_by('date')
    dict={'cjobs':list_of_jobs}
    return render(request,'jobsapp/chennaijobs.html',context=dict)
