from django.db import models

# Create your models here.\
class Student(models.Model):
	genders= [('Female','Female'),('Male','Male'),('Others','Others')]
	fname = models.CharField(max_length=40)
	lname = models.CharField(max_length=30)
	name = models.CharField(max_length=25)
	rnum = models.CharField(max_length=25)
	email = models.EmailField()
	mobile = models.CharField(max_length=10)
	gender = models.CharField(max_length=15,choices=genders)
	age = models.IntegerField(null=True)

	def __str__(self):
		return self.name+''+self.email


