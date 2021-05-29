from django.shortcuts import render
from .models import Exam

# Create your views here.
def index(request):
    exam=Exam.objects.all()
    #dests = Product.objects.all()


    return render(request,"index.html",{'dests': exam})
