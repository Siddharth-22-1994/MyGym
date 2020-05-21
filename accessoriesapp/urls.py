from . import views
from django.urls import path

urlpatterns = [
    path('accessoriesview', views.accessoriesview, name='accessoriesview'),
    path('addacessories', views.addaccessoriesview, name='addacessories'),
]