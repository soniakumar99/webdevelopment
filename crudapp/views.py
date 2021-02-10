from django.shortcuts import render,redirect
from django.http import HttpResponse
from crudapp.models import Student

# Create your views here.
def demo(request):
		return HttpResponse('from crudapp.....')

def addstudent(request):
	if request.method == 'POST':
		fn = request.POST.get('fname')
		ln = request.POST.get('lname')
		un = request.POST.get('uname')
		r = request.POST.get('rnum')
		e = request.POST.get('email')
		m = request.POST.get('mobile')
		g = request.POST.get('gender')
		a = request.POST.get('age')
		Student.objects.create(fname=fn,lname=ln,name=un,rnum=r,email=e,mobile=m,gender=g,age=a)
		return HttpResponse('Record succesfully')
	return render(request,'crudapp/addstudent.html')

def details(request):
	info = Student.objects.all()
	#context={'info':info}
	return render(request,'crudapp/details.html',{'info':info})

def update(request,id):
	data = Student.objects.get(id=id)
	if request.method == 'POST':
		data.fname = request.POST['fname']
		data.lname = request.POST['lname']
		data.uname = request.POST['uname']
		data.rnum = request.POST['rnum']
		data.email = request.POST['email']
		data.mobile = request.POST['mobile']
		data.gender = request.POST['gender']
		data.age = request.POST['age']
		data.save()
		return redirect('/details')
	return render(request,'crudapp/update.html',{'data':data})
def delete(request,id):
	obj=Student.objects.get(id=id)
	if request.method == 'POST':
		obj.delete()
		return redirect('details')
	return render(request,'crudapp/delete.html',{'obj':obj})