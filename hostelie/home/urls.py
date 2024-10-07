
from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='outing'),
    #path('',views.index,name='login'),
    path('',views.index,name='outpass'),	
    path('',views.index,name='home'),
    path('',views.index,name='homepage'),
    ]