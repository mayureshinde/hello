from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact, Registration
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    

def services(request):
    return render(request, 'services.html')
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return render(request, 'login2.html')

    return render(request, "login2.html")

def logoutUser(request):
    logout(request)
    return redirect("login")    

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gstin = request.POST.get('gstin')
        client = Registration(name=name, email=email, phone=phone, address=address, gstin=gstin, date= datetime.today())
        client.save()
        messages.success(request, 'Your registration process has been started')
    return render(request, "registration.html")