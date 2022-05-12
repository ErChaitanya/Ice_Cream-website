import email
from django.shortcuts import render, HttpResponse
from matplotlib.style import context
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# render - It is used to render a templete.

## Create your views here.
##this is url dispatching
# def index(request):
#     return HttpResponse("This is homepage")
    ##kisi bhi string ke request ko run karne ke liye httpresponse ki need hoti hai.
def index(request):
    #this context is basically came for variable handling and calling  which we add in index.html
    context = {
        "variable1" : "Harry is great",
        "variable2" : "Rohan is great"
# variables - this is used for sending models and blogs 

    }
    messages.success(request, "This is a test message.")
    return render(request, 'index.html', context)
    ## This is the function that we made for rendering the file from template named as index.html render ka format pehle hota hai request aur fir hota hai file name.


def about(request):
    return render(request, 'about.html')

    # return HttpResponse("This is about page")


def services(request):
    # return HttpResponse("This is services page")
    return render(request, 'services.html')

    
def contact(request):
    # return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email=email,phone=phone, desc=desc, date = datetime.today())# creating object of contact
        contact.save()
        messages.success(request, 'Your response has been sent!.')

    return render(request, 'contact.html' )
