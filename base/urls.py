from django.urls import path,include 
from . import views



urlpatterns = [
   path('login/',views.login , name='login'),
   path('update/',views.update , name='update'),
   path('add_card/',views.add_card , name='add_card'),
   path('email_password/',views.email_password , name='email_password'),
   path('',views.home , name='home')
]





