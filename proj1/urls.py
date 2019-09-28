from django.conf.urls import url
from .import views

urlpatterns = [
url(r'$^', views.home, name='home'),
url('Home', views.Home, name='Home'),
url('main', views.main, name='main'),
url('after_login',views.after_login,name='after_login'),
# url('onclickauto',views.onclickauto,name='onclickauto'),
url('AboutUs', views.AboutUs, name='AboutUs'),
url('ContactUs', views.ContactUs, name='ContactUs'),
url('Register', views.Register, name='Register'),
url('Login', views.Login, name='Login'),
url('firstpage', views.firstpage, name='firstpage'),
url('second',views.second,name='second'),
url('Logout',views.Logout, name='Logout'),


]

            