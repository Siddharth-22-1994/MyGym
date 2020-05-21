from . import views
from django.urls import path

urlpatterns = [
    path('ByeProdpage', views.ByeProdpage, name='ByeProdpage'),
    path('UserPurchaedPrd', views.UserPurchaedPrd, name='UserPurchaedPrd')
]