from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import math,random
from django.core.mail import send_mail

# Create your views here.
def login(request):
    if request.method == 'POST':
       username=request.POST['user_email']
       password = request.POST['user_password']

       user= auth.authenticate(username=username,password=password)

       if user is not None:
           auth.login(request,user)
           return render(request,'home.html')
       else:
           messages.info(request,'Invalid user')
           return redirect('login')


    else:
      return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
def register(request):
    if request.method== 'POST':
       username = request.POST['first_name']
       email = request.POST['email']
       mobile = request.POST['mobile']
       password1 = request.POST['password1']
       password2 = request.POST['password2']
       if password1==password2:
          if User.objects.filter(email=email).exists():
             messages.info(request,'user already exist')
             return redirect('register')
          else:
             user= User.objects.create_user(first_name=username,username=email,email=email,password=password1)
             user.save();
             return redirect('login')
    else:
        return render(request,'login.html')
'''
def password_reset(request):
    if request.method=='POST':
        pass1=request.POST['new_pass']
        pass2=request.POST['confrm_pass']
        code=request.POST['otp']
        if pass1==pass2:
            redirect('login')
    else:
        string = '01234567890123456789'
        OTP = ""
        length = len(string)
        for i in range(6):
            OTP += string[math.floor(random.random() * length)]

        render(request,'password_reset.html')
        '''


