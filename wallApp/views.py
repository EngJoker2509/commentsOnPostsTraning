from django.shortcuts import render, HttpResponse, redirect
from .models import *
from loginAndRegApp.models import *

def index(request):
    if not 'userid' in request.session:
        return redirect('/')
    if request.method == 'POST':
        messages.create_message(request)
        return redirect('/thewall')
    else:
        context = {
            'all_messages': messages.retrive_last_3_messages()
        }
        return render(request, 'index1.html', context=context)

def wall(request):
    if not 'userid' in request.session:
        return redirect('/')
    if request.method == 'POST':
        comments.create_comment(request)
        return redirect('/thewall/wall')
    else:
        context = {
            'all_messages' :messages.retrive_last_3_messages(),
            'all_comments': comments.retrive_All_comments()
        }
        return render(request, 'wall.html', context=context)

def destroy(request):
    if not 'userid' in request.session:
        return redirect('/')
    del request.session['userid']
    del request.session['LoginAuth']
    return redirect('/')