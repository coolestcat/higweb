# myapp/api.py
from tastypie.resources import ModelResource
from web.models import Entry

class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'