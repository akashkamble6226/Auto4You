from django.conf.urls import url
from .import views

urlpatterns = [
url(r'$^', views.home, name='home'),
#url('Base',views.Base,name='Base'),
# url('onclickauto',views.onclickauto,name='onclickauto'),
url('AboutUs', views.AboutUs, name='AboutUs'),
url('ContactUs', views.ContactUs,name='ContactUs'),
url('Register', views.Register, name='Register'),
url('Login', views.Login,name='Login'),
url('second',views.second,name='second')



]

            