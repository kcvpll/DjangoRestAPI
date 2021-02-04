from django.contrib import admin
from .models import Students, Teachers


# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'date', 'group', 'visible')
    list_display_links = ('id', 'name', 'surname', 'group')
    search_fields = ('id', 'name', 'surname', 'date', 'group', 'visible')
    list_editable = ('visible',)
    list_filter = ('visible', 'name', 'date')


class TeachersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'date', 'subject', 'visible')
    list_display_links = ('id', 'name', 'surname', 'subject')
    search_fields = ('id', 'name', 'surname', 'date', 'subject', 'visible')
    list_editable = ('visible',)
    list_filter = ('visible', 'name', 'date')


admin.site.register(Students, StudentsAdmin)
admin.site.register(Teachers, TeachersAdmin)
