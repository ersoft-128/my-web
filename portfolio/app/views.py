from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from app.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import  logout, authenticate , login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.






def loginUser(request):
    if request.method =="POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      print(username,password)
      user = authenticate(username=username, password=password)
      
    
      if user is not None:
          login(request,user)
          return redirect("/")  
      else:
          return render (request, "login.html") 
    return render (request, "login.html") 

def logoutUser(request):
    logout(request)
    return redirect("/login")

def homepage(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

    # return HttpResponse("Home Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        sub = request.POST.get('sub')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email = email, sub = sub,phone = phone, desc = desc, date=datetime.today())
        contact.save()


    return render(request,'base.html')


