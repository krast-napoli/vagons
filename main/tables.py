import django_tables2 as tables
from .models import Trains

class TrainsTable(tables.Table):
    class Meta:    
        model = Trains
        attrs = {"td": {"contenteditable": "true"}}