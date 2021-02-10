"""vitw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sonipavani import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',views.display),
    path('center/',views.centerexample),
    path('right/',views.rightsample),
    path('pavani/',views.soni),
    path('stringvalues/<str:name>/',views.stringvalues),
    path('age/<int:num>',views.age),
    path('samplehtml/',views.samplehtmlex),
    path('demo',views.htmlexcss,name=''),
    path('chinnu',views.external,name=''),
    path('bootex/',views.bootstrapex,name=''),
    path('login/',views.login,name=''),
    path('registration/',views.registration,name=''),
    path('',include('crudapp.urls')),
    path('forms/',include('formsapp.urls')),
]
