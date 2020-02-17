#from django.forms import ModelForm
from django.forms import modelformset_factory, TextInput, DateTimeInput
#from django.forms import TextInput
from .models import Trains

UserForm = modelformset_factory(Trains,
                                fields=(
                                       'ordNumber', 'carNumber', 'trainIndex',
                                       'trainNumber', 'carStatus', 'invoiceId',
                                       'invoiceNumber', 'stateId', 'lastOperDt'
                                       ),
#                                initial=[{'trainIndex': '-',}],
                                widgets={
                                        'ordNumber': TextInput(attrs={'size': 10}),
                                        'carNumber': TextInput(attrs={'size': 10}),
                                        'trainIndex': TextInput(attrs={'size': 20}),
                                        'trainNumber': TextInput(attrs={'size': 10}),
                                        'carStatus': TextInput(attrs={'size': 35}),
                                        'invoiceId': TextInput(attrs={'size': 10}),
                                        'invoiceNumber': TextInput(attrs={'size': 10}),
                                        'stateId': TextInput(attrs={'size': 5}),
                                        'lastOperDt': DateTimeInput(attrs={'size': 15}),
                                         },
                                 can_order=True
                                 )

'''
class Meta:
        model = Trains
        exclude = ['ordNumber']
'''

'''
widgets = {
            'carStatus': textarea(attrs={'cols': 80, 'rows': 20}),
                   }
'''