from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.html')
    # return HttpResponse('this is services page')

