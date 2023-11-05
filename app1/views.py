from django.shortcuts import render

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
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        pass
    else:
        return render(request,'login.html')