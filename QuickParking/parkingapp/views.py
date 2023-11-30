from django.shortcuts import render,HttpResponse
from datetime import datetime
from parkingapp.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    #here the context is the set of variables so i can use them for further reference 
    # context = {
    #     'variable1': "Hello",
    #     'variable2' : "TRP",
    # }
    return render(request, 'index.html') #here i can add the context for the variables for ex: render(request, 'index.html' , context ) 

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
    return render(request,'signup.html')