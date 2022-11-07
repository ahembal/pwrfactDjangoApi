from django.contrib import admin
from .models import Experiment, Record
# Register your models here.
admin.site.register(Experiment)
admin.site.register(Record)