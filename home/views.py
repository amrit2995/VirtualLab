import django
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
import os
from django.conf import settings
import json
from .allforms import ServerForm, loginpage
from .models import Servers
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth import authenticate,logout,login
import logging

# settings.configure()
servers_file = open(os.path.join(settings.STATICFILES_DIRS[0], 'new_servers.json'))
def index(request):
    print(request.user)
    servers = ['CUCM', 'CUC', 'UCCX', 'UCS']
    return render(request,'index.html',{'servers':servers})
# Create your views here.

def get_server_details(request,server_type):
    servers = Servers.objects.filter(server_type=server_type)
    return render(request,'device_type.html',{'servers': servers, 'type': server_type})

def create_device(request,type):
    if request.method == 'POST':
        try:
            form = ServerForm(request.POST)
            new_device = Servers(
                server_type = type,
                hostname = request.POST['ipaddress'],
                password = request.POST['password'],
                ipaddress = request.POST['ipaddress'],
                fqdn = request.POST['fqdn'],
                username = request.POST['username'],
                creator = request.user
            )
            new_device.save()
            return redirect('Cisco_servers', server_type=type)
        except ValueError:
            return render(request, 'new_device_entry.html', {'form':form, 'error':'bad Data passed.'})
    form = ServerForm()
    return render(request,'new_device_entry.html', {'form':form, 'type': type })


@csrf_exempt
def signupuser(request):
    form = UserCreationForm()
    if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                username = request.POST['username']
                password = request.POST['password1']
                try:
                    user = User.objects.create_user(request.POST['username'],request.POST['password1'])
                    user.save()
                    login(request,user)
                    return render(request, 'index.html')
                except IntegrityError:
                    return render(request,'signup.html',{'form':form,'error':'Already a match exists'})                    
            else :
                return render(request,'signup.html',{'form':form,'error':'Passwords did not match'})

    return render(request,'signup.html', {'form':form})

@csrf_exempt
def logging(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'login.html', {'form':AuthenticationForm(),'error':"Username or password incorrect."})
        else: 
            login(request,user)
            return redirect('index')


@csrf_exempt
def loggingout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')




