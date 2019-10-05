
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

from django.contrib import messages
from .models import from_Malegaon_College,from_MalegaonBK,from_Shardanagar,from_Baramati 
import urllib.request
import urllib.parse





#from .models import Data

# Create your views here.


def home(request): 
    return render(request,'firstpagenew.html') # for viewing it first time

def Home(request): 
    return render(request,'firstpage.html') # for comming back to home from any page



def firstpagenew(request): 
    return render(request,'firstpagenew.html')
def main(request): 
    return render(request,'main.html')


def Register(request):
    if request.method=='POST':
        print('Into the post now') 
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            # print("Username Taken")
            messages.info(request,'Username Taken')
            
            return redirect('Register')
            
        elif User.objects.filter(email=email).exists():
            # print("Email Taken")
            messages.info(request,'Email Taken')
            return redirect('Register')
            
        else:
            user = User.objects.create_user(first_name=first_name,email=email,username=username,password=password)
            user.save()
            # print ('User Created')
            messages.success(request,'User has been created !')
            # return redirect('/')
            return redirect('Register')

    else:
        return render(request,'Register.html')
        
        
        
    
        






def onclickauto(request):
    return render(request,'onclickauto.html')

def AboutUs(request):
    if request.method=='POST':
        Data =request.get("sms2.py")
        print(Data)
        print=Data.text
        return render(request,'AboutUs.html',{'data':Data})
    else:
        return render(request,'AboutUs.html')
        
    

def ContactUs(request):
    return render(request,'ContactUs.html')



def Login(request):
    if request.method=='POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("main")
        else:
            messages.success(request,'Invalid Credentials')
            return redirect("Login.html")
    else:
        return render(request,"Login.html")


def after_login(request):
    return render(request,'after_login.html')

def Logout(request):
    auth.logout(request)
    return redirect("firstpagenew.html")

def final(request):
    return render(request,'final.html')




def Sendsmsroute(request):
    resp =  sendSMS('dgDpU4wgcrk-UfUgKP7CLLl28GHbIP3Vl5vlrBeah6', '8669325226','TXTLCL', 'Location:Malegaon College')
    print (resp)
   
    start_loc = from_Malegaon_College(start_loc='Malegaon College') #for storing entry into from_Malegaon_College
    start_loc.save()
    return HttpResponse(request,"final.html")
    
   


def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()

    return(fr)

def Sendsmsroute1(request):
    resp =  sendSMS('dgDpU4wgcrk-UfUgKP7CLLl28GHbIP3Vl5vlrBeah6', '8669325226','TXTLCL', 'Location:Malegaon BK')
    print (resp)
   
    start_loc = from_MalegaonBK(start_loc='Malegaon Bk') #for storing entry into from_Malegaon_Bk
    start_loc.save()
    

    
    return HttpResponse("Msg sent")

def Sendsmsroute2(request):
    resp =  sendSMS('dgDpU4wgcrk-UfUgKP7CLLl28GHbIP3Vl5vlrBeah6', '8669325226','TXTLCL', 'Location:Shardanagar')
    print (resp)
   
    start_loc = from_Shardanagar(start_loc='Shardanagar') #for storing entry into from_Shardanagar
    start_loc.save()
    

    
    return HttpResponse("Msg sent")

def Sendsmsroute3(request):
    resp =  sendSMS('dgDpU4wgcrk-UfUgKP7CLLl28GHbIP3Vl5vlrBeah6', '8669325226','TXTLCL', 'Location:Baramati')
    print (resp)
   
    start_loc = from_Baramati(start_loc='Baramati') #for storing entry into from_Shardanagar
    start_loc.save()
    

    
    return HttpResponse("Msg sent")



    
def forgotpassword(request):
    if request.method=='POST':
        un = request.POST['uname']
        np = request.POST['npassword']
        cp = request.POST['cpassword']
        if User.objects.filter(username=un).exists():
            if np == cp:
                print("Yes")
                User.objects.set_password(np)
                save()
               
                messages.success(request,'Password has been reset successfully ')
                return render(request,"forgotpassword.html")
            else:
                print("no")
                messages.info(request,'Password mismatch')
                return render(request,"forgotpassword.html")
        else:
            messages.info(request,'Username not found ')
            return render(request,"forgotpassword.html")
        
    else:
        
        return render(request,'forgotpassword.html')
    
    


    
    








