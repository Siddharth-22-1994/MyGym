from . import views
from django.urls import path

from .views import signup

urlpatterns = [
    path('accounts/register/', signup, name='signup'),
]