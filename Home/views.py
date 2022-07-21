from django.shortcuts import render,HttpResponse
from Home.models import response
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request,'index.html') 
    #return HttpResponse('This is Home page')

def Home(request):
    return render(request,'index.html')
    #return HttpResponse('This is home page')

# def about(request):
#     return render(request,'aboutus.html') 
#     #return HttpResponse('This is about page')

def competitions(request):
     return render(request,'Competitions.html') 
    #return HttpResponse('This is competitions page')

def contact(request):
    if request.method == "POST":
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = response(email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!') 
    return render(request,'contact.html') 
    # return HttpResponse('This is contact page')    

def profile(request):
    return render(request,'profile.html') 

# def journal(request):
#     return render(request,'journal.html')       

def about(request):
    return render(request,'about.html')