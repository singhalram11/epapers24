from django.shortcuts import render
from .models import hackerrank
# Create your views here.
def tutorial(request):
    prob=hackerrank.objects.only('name')


    print(val)
    solution=hackerrank.objects.all()
    return render(request,'tutorial.html',{'prob':prob,'solutions':solution})

def newpage(request):
    return render(request,'newpage.html')