from django.urls import path

from userloginapp.views import userlogin, userlogout

urlpatterns = [
    path('accounts/login/', userlogin, name='userlogin'),
    path('accounts/logout/', userlogout, name='userlogout')
]