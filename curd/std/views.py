from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import student
from .forms import StudentForm
# Create your views here.


def add(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        name=form.cleaned_data.get('name')
        return redirect('create')

    else:
        form=StudentForm()
        st=student.objects.all()
    return render(request,'std/create.html',{'form':form,'st':st})




def update(request,id):
    if request.method=='POST':
        d=student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=d)
        if fm.is_valid():
            fm.save()
        return redirect("create")
    else:
        d=student.objects.get(pk=id)
        fm=StudentForm(instance=d)
    return render(request,'std/update.html',{'fm':fm})



def delete(request,id):
    if request.method=='POST':
        d=student.objects.get(pk=id)
        d.delete()
        return redirect('create')


