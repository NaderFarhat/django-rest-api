from django.contrib import admin
from .models import Events, Noc
from import_export import resources

# Register your models here.

class NocResource(resources.ModelResource):

    class Meta:
        model = Noc
        skip_unchanged = True
        report_skipped = False
        fields = [
            'noc',
            'region',
            'notes'
        ]

admin.site.register(Events)
admin.site.register(Noc)