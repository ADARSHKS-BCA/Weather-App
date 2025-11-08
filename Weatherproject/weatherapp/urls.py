# Will write all the urls of the base app 
# When importing the urls from the same app or the project we use the . import views insted of django.views 

from . import views
from django.urls import path 

urlpatterns = [
    path('',views.home),
]