from django.shortcuts import render
#from .forms import UserForm
from .forms import UserFormSet

def index (request):
    userform = UserFormSet(initial=[
    {'name':'John', 'age':'20'},
    {'name':'Ben', 'age':'21'}
    ]) # or userform = UserForm()
    return render (request, 'main/mainPage.html', {"form": userform})

#from django.shortcuts import render
#from .tables import PersonTable
#from .models import Person


#def person_list (request):
#    table = PersonTable(Person.objects.all())

#    return render(request, 'trytables/mainPage.html', {'table':table})