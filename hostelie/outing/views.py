from django.shortcuts import render
#from django.http import HttpResponse
from .models import outt
def index(request):
	if request.method=='post':
		name=request.POST['name']
		plf=request.POST['plf']
		
		user=User.objects.create_user(name=name,plf=plf)
		user.save();	
	return render(request,'outing.html')