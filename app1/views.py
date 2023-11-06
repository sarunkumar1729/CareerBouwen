from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import User
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile
from django.http import FileResponse

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

def profile(request):
    if request.method=='POST':
        permanantAddress=request.POST['permanantAddress']
        currentAddress=request.POST['currentAddress']
        phone1=request.POST['phone1']
        phone2=request.POST['phone2']
        photo=request.FILES.get('photo')
        education=request.POST['education']
        skills=request.POST['skills']
        resume=request.FILES.get('resume')
        user=request.user
        # print(permanantAddress,currentAddress,phone1,phone2,photo,education,skills,resume)
        new_profile=UserProfile(
            profile_user=user,
            current_address=currentAddress,
            permanant_address=permanantAddress,
            phone1=phone1,
            phone2=phone2,
            photo=photo,
            Education=education,
            skills=skills,
            resume=resume
        )
        new_profile.save()
        print('success')
        return redirect('index')
    else:
        user=request.user
        profile=UserProfile.objects.get(profile_user=user)
        return render(request,'profile.html',{"profile":profile})


def edit_profile(request):
    if request.method=='POST':
        pass
    else:
        return render(request,'edit_profile.html')
