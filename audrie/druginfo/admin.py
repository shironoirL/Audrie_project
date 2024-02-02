from django.contrib import admin
from .models import DrugInformation


@admin.register(DrugInformation)
class PostAdmin(admin.ModelAdmin):
    list_display = ['drugname', 'drugbankID', 'moleculeType', 'status']

# Register your models here.
