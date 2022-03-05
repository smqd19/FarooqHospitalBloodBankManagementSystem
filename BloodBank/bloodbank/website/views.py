from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # send an email
        send_mail(
            'Django Testing from Bitcoin Exchange', #subject
            message, #message
            email, #from email
        ['q.shaikh14@gmail.com'], #to email
        )
        return render(request, 'contactus.html', {'name':name,'message':message})
    else:
        return render(request, 'contactus.html', {})

def charts(request):
    return render(request, 'chartpage.html', {})