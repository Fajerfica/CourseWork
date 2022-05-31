from django.contrib import admin
from .models import Algos, Problems, HistoryRecord
# Register your models here.

admin.site.register(Algos)
admin.site.register(Problems)
admin.site.register(HistoryRecord)