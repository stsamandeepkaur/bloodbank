from django.shortcuts import render
from Myapp.forms import DonorForm, ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from Myapp.models import Donor

def index(request):
    data = ContactForm(request.POST)

    if request.method == 'POST':
        data = ContactForm(request.POST)

        if data.is_valid():
            data.save(commit=True)
            return HttpResponse("Thanks")
            print('saved successfully')
            # messages.success(request, 'Form submission successful')


    return render(request,'index.html',{'contact':data})

def donors(request):
    data = Donor.objects.order_by('id')
    return render(request,'donor.html',{'records':data})

def donor(request):
    form = DonorForm

    if request.method == 'POST':
        form = DonorForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect('/')

    return render(request,'donorRegisteration.html',{'form':form})
