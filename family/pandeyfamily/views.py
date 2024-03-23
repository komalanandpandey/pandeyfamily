from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'public/index.html', {'header': 'HOME'})


def login(request):
    return render(request, 'login.html', {'header': 'Login'})


def about(request):
    return render(request,'about.html',{'header':'About MyVillage'})


def contactus(request):
    return render(request,'contactus.html',{'header':'contactus'})


def video(request):
    return render(request,'video.html',{'header':'video'})


def kuldevta(request):
    return render(request,'kuldevta.html',{'header':'kuldevta'})


def vanshavali(request):
    return  render(request,'vanshavali.html',{'header':'vanshavali'})
