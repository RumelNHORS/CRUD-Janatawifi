from django.shortcuts import render, HttpResponseRedirect
from . forms import CustomerRegistrationForm
from django.contrib import messages
from . models import User, JsonModel
from django.http import JsonResponse
import json
from django.views.generic import ListView


#This is For Add new Item ans Show The new item on Frontin
def add_show(request):
    if request.method == 'POST':
        fm = CustomerRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = CustomerRegistrationForm()
            messages.success(request, 'Form submission successful')
    else:
        fm = CustomerRegistrationForm()
    stu = User.objects.all()
    return render(request, 'myapp/addandshow.html', {'form': fm, 'stu':stu})

#This Function is For Update/Edit Data
def update_data(request, id):
    if request.method == 'POST':
        up = User.objects.get(pk=id)
        fm = CustomerRegistrationForm(request.POST, instance=up)
        if fm.is_valid():
            fm.save()
    else:
        up = User.objects.get(pk=id)
        fm = CustomerRegistrationForm(instance=up)
    return render(request, 'myapp/update.html', {'form':fm})

#This Function is For Detele Item
def delete_data(request, id):
    if request.method == 'POST':
        de = User.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/')

#This is Model to JSON View Function
def JsonView(request):
    data = list(JsonModel.objects.values())
    return JsonResponse(data, safe=False)
