from django.urls import path
from crudapp import views
urlpatterns=[
	path('demo1/',views.demo),
	path('addstudent/',views.addstudent,name='addstudent'),
	path('details/',views.details,name='details'),
	path('updatepage/<int:id>/',views.update,name='update'),
	path('deletepage/<int:id>/',views.delete,name='delete'),
	# path('main/',)
]