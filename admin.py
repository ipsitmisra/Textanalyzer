from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(inputtext)
class user_data(ImportExportModelAdmin):
    search_fields = ['text']