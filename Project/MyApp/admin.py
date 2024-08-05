from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import EmpD
# Register your models here.

@admin.register(EmpD)
class EmpDAdmin(ImportExportActionModelAdmin):
    list_display = ('EId', 'Gender', 'Experience', 'Position', 'Salary') 