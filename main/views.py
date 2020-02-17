from django.shortcuts import render
from .forms import UserForm
from .models import Trains
#from .tables import TrainsTable
from django.http import HttpResponseRedirect

def main (request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form.save()
        return HttpResponseRedirect ("/main")
    else:
        form = UserForm()
    return render (request, 'main/mainPage.html', {"form": form})

'''
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
'''