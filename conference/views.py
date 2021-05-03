from django.shortcuts import render, redirect
from .models import Participant

# Create your views here.

def index(request):
    participants = Participant.objects.all()
    context = {'participants': participants}
    return render(request, 'registration.html', context)

def registration(request):

    if "register" in request.POST:
        participant = Participant(fullname=request.POST["fullname"], 
        emails = request.POST['emails'],
        phone = request.POST['phone'],
        address = request.POST['address'],
        capacity = request.POST['capacity'],
        title = request.POST['title'],
        description = request.POST['description']
        )
        participant.save()
        return redirect('/')

    return render(request,'registration.html')

def maps(request):
    return render(request, 'maps.html')

def index(request):
    return render(request,'index.html')