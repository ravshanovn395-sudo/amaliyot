from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

def create_student(request):
    form = StudentForm(request.POST or None,request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect ('student-list')
    return render(request,'create.html',{'forms':form})

def student_list(request):
    pro = Student.objects.all()
    return render(request,'update.html',{'pro':pro})


def update_student(request,id):
    imp = Student.objects.get(id=id)
    forms = StudentForm(request.POST or None ,request.FILES or None,instance=imp)
    if request.method == 'POST' and forms.is_valid():
        forms.save()
        return redirect('product-view')
    return render(request, 'update.html', {'forms':forms})