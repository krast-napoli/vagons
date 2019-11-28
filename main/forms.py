from django.forms import ModelForm
from .models import Trains

class UserForm(ModelForm):
    class Meta:
        model = Trains
        exclude = ['OrdNumber']