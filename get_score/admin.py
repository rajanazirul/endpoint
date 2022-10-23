from django.contrib import admin
from . import models

class RecordFilter(admin.ModelAdmin):
    list_display=['user_id', 'input_one', 'result', 'created']
    list_editable=['input_one', 'result']
    search_fields=['user_id', 'input_one', 'result', 'created']
# Register your models here.
admin.site.register(models.Record, RecordFilter)
