from django.shortcuts import render
from .forms import UserForm
from .models import Trains
from .tables import PersonTable
from django.http import HttpResponseRedirect

#def index (request):
#    userform = UserForm()
#    return render (request, 'main/mainPage.html', {"form": userform})

def trains_list (request):
    table = TrainsTable(Trains.objects.all())

    return render(request, 'main/mainPage.html', {'table':table})

def create_new (request):
    if request.method == "POST":
        f = UserForm(request.POST)
        a = Trains.objects.get(pk=1)
        f = UserForm(request.POST, instance=a)
        f.save()
    return HttpResponseRedirect ("/main")