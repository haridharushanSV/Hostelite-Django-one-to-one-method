from django.shortcuts import render
#from django.http import HttpResponse
from .models import outp
def index(request):
	if request.method=='post':
		name=request.POST['name']
		plf=request.POST['plf']
		

		obj=outp()
		obj.name=name
		obj.plf=plf

		obj.save()
	return render(request,'outpass.html')