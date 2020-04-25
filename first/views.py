from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import branch
# Create your views here.
def home(request):
       if request.method=='POST':
           branches = branch.objects.all()
           return render(request, 'home.html', {'branches': branches})

       else:

           return redirect('login')

