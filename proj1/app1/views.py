from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def create_view(request):
    template_name = 'app1/Add_new.html'
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def show_view(request):
    obj = Employee.objects.all()
    template_name = 'app1/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def update_view(request, pk):
    obj = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=obj)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'app1/Update.html'
    context = {'form': form}
    return render(request, template_name, context)

def delete_view(request, pk):
    template_name = 'app1/delete.html'
    obj = Employee.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    context = {'obj': obj}
    return render(request, template_name, context)
