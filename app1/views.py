from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import User

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
        print(username,firstname,lastname,email,password,confirmPassword)
        return redirect('login')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        pass
    else:
        return render(request,'login.html')
    

def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        
        if username is not None:
            user_exists = User.objects.filter(username=username).exists()
            return JsonResponse({'exists': user_exists})

    return JsonResponse({'error': 'Invalid request'}, status=400)
