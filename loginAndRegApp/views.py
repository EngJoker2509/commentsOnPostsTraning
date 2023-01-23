from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


def form_page(request):
    if not 'LoginAuth' in request.session:
        request.session['LoginAuth']=""
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validtor(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        Register(request)
    return redirect('/')

def login(request):
    if request.method == "POST":
        if Login(request):         
            return redirect('/thewall')
    return redirect('/')

def clear(request):
    del request.session['userid']
    del request.session['LoginAuth']
    return redirect('/')
