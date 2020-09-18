from django.shortcuts import render, redirect
from .models import listing_model
from .forms import listing_form
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
#from testapp.models import Signup

# Create your views here.
@login_required
def listing(request):
    if request.method=='POST':
        form=listing_form(request.POST, request.FILES)
        if form.is_valid():
            form1=form.save(commit=False)
            form1.author=request.user
            form1.save()
            return redirect('submissions')
        return render(request, 'listing_upload.html', {'form' : form})
    else:
        form=listing_form()
    return render(request, 'listing_upload.html', {'form' : form})

# My Submissions
@login_required
def submissions(request):
    tasks=listing_model.objects.filter(author=request.user)
    form = listing_form()
    if request.method =='POST':
        form = listing_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('submissions')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'submission.html', context)

def updateTask(request, pk):
    task = listing_model.objects.get(id=pk)
    form = listing_form(instance=task)
    if request.method == 'POST':
        form = listing_form(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
        return redirect('submissions')
    context = {'form':form}
    return render(request, 'updatepg.html', context)

def deleteTask(request, pk):
    item = listing_model.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('submissions')
    context = {'item':item}
    return render(request, 'deletepg.html', context)


#ajax
def contact(request, id):
        numbers = listing_model.objects.get(id=id)
        return JsonResponse({'numbers': numbers.phone})
  