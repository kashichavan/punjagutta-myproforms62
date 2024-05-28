from django.shortcuts import render,HttpResponse
from .forms import StudentForm
# Create your views here.
from .models import StudentModel

# with form validation
def register(request):
    if request.method=='POST':
        form=StudentForm(request.POST) # sending dict object into form object
        if form.is_valid():  # checking form is valid
            a=request.POST.get('email') # extracting values of key
            b=request.POST.get('first_name')
            c=request.POST['last_name']
            d=request.POST['age']
            obj=StudentModel(email=a,first_name=b,last_name=c,age=d) #creating model object
            obj.save() # storing by using save
        return HttpResponse("<h1>Form submitted suceessssszfull</h1>")
    else:
        form=StudentForm()
        data={'form':form}
        return render(request,'form.html',context=data)

# without validation   
def register1(request):
    if request.method=='POST':
        a=request.POST.get('email')
        b=request.POST.get('first_name')
        c=request.POST['last_name']
        d=request.POST['age']
        obj=StudentModel(email=a,first_name=b,last_name=c,age=d)
        obj.save()
        return HttpResponse("<h1>Form submitted suceessssszfull</h1>")
    else:
        form=StudentForm()
        data={'form':form}
        return render(request,'form.html',context=data)
    
