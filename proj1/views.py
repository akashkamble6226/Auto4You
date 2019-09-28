
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Data as data
import urllib.request
import urllib.parse
from flask import Flask
from flask import render_template
app = Flask(__name__)



#from .models import Data

# Create your views here.


def home(request): 
    return render(request,'firstpage.html') # for viewing it first time

def Home(request): 
    return render(request,'firstpage.html') # for comming back to home from any page



def firstpage(request): 
    return render(request,'firstpage.html')
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
        
        
        
    
        

def second(request):
    source1 = request.POST['source']
    dest1 = request.POST['dest']
    #var = [source1 , dest1]
    return render(request,'secondpage.html',{'source':source1, 'dest':dest1})




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
    return redirect("firstpage.html")



@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/sendSMS')


def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS('Zro10KL6WX4-YcI8DJDBXczWANsTKV1X37omKg8Mf2', '918605719895',
    'TXTLCL', 'This is your message')
print (resp)



