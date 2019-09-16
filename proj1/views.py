
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Data,Check


#from .models import Data

# Create your views here.
def home(request): 
    return render(request,'firstpage.html')

# def Trying(request):
#     print(request.headers)
#     return render(request,"AboutUs.html")

def Register(request):
    return render(request,'Register.html')
    # if request.method=='POST':
    #     print('Into the post now') 
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     email = request.POST['email']
    #     username = request.POST['username']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['Re_password2']

    #     user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password1=password1)
    #     check = Check.objects.create_user(first_name=first_name,last_name=last_name)
    #     data.save();
    #     print ('User Created')
    #     return redirect('/')
    # else: 
        

def second(request):

    source1 = request.POST['source']
    dest1 = request.POST['dest']
    #var = [source1 , dest1]
    return render(request,'secondpage.html',{'source':source1, 'dest':dest1})




def onclickauto(request):
    return render(request,'onclickauto.html')

def AboutUs(request):
    return render(request,'AboutUs.html')

def ContactUs(request):
    return render(request,'ContactUs.html')



def Login(request):
    return render(request,'Login.html')




