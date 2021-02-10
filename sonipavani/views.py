from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
	return HttpResponse("<h1>welcome to django session</h1>")


def centerexample(request):
	return HttpResponse("<center> <h1>welcome vitw</h1> </center>" )


def rightsample(request):
	return HttpResponse("<right> <h1> goodmorning</h1> </right>")

def soni(request):
	return HttpResponse("<pavani> <h1>django session</h1><br><br><h2> this is pavani</h2> ")	


def stringvalues(request,name):
	return HttpResponse("helloooo..........."+name)

def age(request,num):
	return HttpResponse("age is....%d"%num)

def samplehtmlex(request):
	return render(request,'sonipavani/sample.html')

def htmlexcss(request):
	return render(request,'sonipavani/demo.html')

def external(request):
	return render(request,'sonipavani/chinnu.html')
def bootstrapex(request):
	return render(request,'sonipavani/bootstrapex.html')

def login(request):
	return render(request,'sonipavani/login.html')

def registration(request):
	if request.method=='POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		username = request.POST.get('username')
		rollno = request.POST.get('rollno')
		email = request.POST.get('email')
		password = request.POST.get('password')
		mobile = request.POST.get('mobile')
		#print(fname,lname,username)
		return render(request,'sonipavani/details.html',{'fname':fname,'lname':lname,'username':username,'rollno':rollno,'email':email,'password':password,'mobile':mobile})
	return render(request,'sonipavani/registration.html')