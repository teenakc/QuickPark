from django.shortcuts import render,HttpResponse , redirect
from datetime import datetime
from parkingapp.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import logout,authenticate,login


# Create your views here.
#user password @TRPcpm123#



def index(request):
    #here the context is the set of variables so i can use them for further reference 
    # context = {
    #     'variable1': "Hello",
    #     'variable2' : "TRP",
    # }
    
    if request.user.is_anonymous:
        return redirect("/login")

    username = request.user.username
    return render(request, 'index.html',{'username': username}) #here i can add the context for the variables for ex: render(request, 'index.html' , context ) 

def about(request):
    
    return render(request,'about.html')
    # return HttpResponse('this is about page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "We received your message soon we will contact with you")
        

    return render(request,'contact.html')
    # return HttpResponse('this is services page')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        data = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        data.save()
        # messages.success(request, "Account Created Successfully return to login page !")
        return redirect('login')

        
    return render(request,'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        password = str(password)
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            messages.warning(request,"Sorry you entered the wrong credential please make sure you have an account")


        
            
        
    return render(request, "login2.html")

def logoutUser(request):
    logout(request)
    return redirect('/login')