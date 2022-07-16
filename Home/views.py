from email import message
from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact

# Create your views here.
def index(request):
    # return HttpResponse("This is Homepage")
    return render(request, "home/index.html")


def about(request):
        return render (request, "home/about.html")
def service(request):
        return render (request, "home/services.html")

def blog(request):
        return render (request, "blog/blogHome.html")

def contact(request):
        if request.method == "POST":
                name= request.POST.get('name')
                email= request.POST.get('email')
                subject= request.POST.get('subject')
                message= request.POST.get('message')
                contact = Contact (name=name, email=email, subject= subject, message= message,
                           date= datetime.today())
                contact.save()

        return render(request, "home/contact-us.html")




  