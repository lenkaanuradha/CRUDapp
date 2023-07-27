from django.shortcuts import render,HttpResponseRedirect
from .forms import Studentform
from .models import Student
# This function will add and show Student Details
def addshow(request):
 
 if(request.method=='POST'):
  fm=Studentform(request.POST)
  if (fm.is_valid()):
#    fm.save()
#    or
   nm=fm.cleaned_data['Name']
   em=fm.cleaned_data['Email']
   pw=fm.cleaned_data['password']
   reg=Student(Name=nm,Email=em,password=pw)
  
   reg.save()
   fm=Studentform()
 else:
  fm=Studentform()
 stud=Student.objects.all()
 return render(request,'myapp/addandshow.html',{'form':fm,'stu':stud})
def update(request,id):
  if request.method=='POST':
   pi=Student.objects.get(pk=id)
   fm=Studentform(request.POST,instance=pi)
   if fm.is_valid():
    fm.save()
  else:
   pi=Student.objects.get(pk=id)
   fm=Studentform(instance=pi)
  return render(request,'myapp/update.html',{'updateform':fm})
def delete_data(request,id):
 if request.method == 'POST':
 
  pi=Student.objects.get(pk=id)
  pi.delete()
  
 return HttpResponseRedirect('/')