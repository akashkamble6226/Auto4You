from django.conf.urls import url
from .import views

urlpatterns = [
url(r'$^', views.home, name='home'),
url('Home', views.Home, name='Home'),
url('main', views.main, name='main'),
url('after_login',views.after_login,name='after_login'),

url('AboutUs', views.AboutUs, name='AboutUs'),
url('ContactUs', views.ContactUs, name='ContactUs'),
url('Register', views.Register, name='Register'),
url('Login', views.Login, name='Login'),
url('firstpagenew', views.firstpagenew, name='firstpagenew'),

url('Logout',views.Logout, name='Logout'),

url('sendSMS',views.Sendsmsroute, name='sendSMS(numbers, sender, message)'), #from malegaon clg

url('Sendsmsroute1',views.Sendsmsroute1, name='Sendsmsroute1(numbers, sender, message)'), #from malegav bk

url('Sendsmsroute2',views.Sendsmsroute2, name='Sendsmsroute2(numbers, sender, message)'),# from Shardanagar

url('Sendsmsroute3',views.Sendsmsroute3, name='Sendsmsroute3(numbers, sender, message)'),# from Baramati

url('forgotpassword',views.forgotpassword, name='forgotpassword'),

url('final',views.final,name='final'),



]

            