from django.shortcuts import render
from django.http import HttpResponse
from formsapp.forms import StudentForm

# Create your views here.
def demo(request):
	return HttpResponse('iam from formapp')
def reg(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		form.save()
		return HttpResponse('data inserted using forms')
	form = StudentForm()
	return render(request,'formsapp/reg.html',{'form':form})