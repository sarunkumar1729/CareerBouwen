from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstName']
        lastname=request.POST['lastName']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['password1']
        # print(username,firstname,lastname,email,password,confirmPassword)
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save()
        print('success')
        return redirect('userlogin')
    else:
        return render(request,'register.html')
    
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def userlogout(request):
    logout(request)
    return redirect('index')

def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        
        if username is not None:
            user_exists = User.objects.filter(username=username).exists()
            return JsonResponse({'exists': user_exists})

    return JsonResponse({'error': 'Invalid request'}, status=400)
