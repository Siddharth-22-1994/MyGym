from . import views
from django.urls import path

urlpatterns = [
    path('adminproj', views.admin, name='adminproj'),
    path('admincheck', views.admincheck, name='admincheck'),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('adminusertab', views.adminusertab, name='adminusertab')
]