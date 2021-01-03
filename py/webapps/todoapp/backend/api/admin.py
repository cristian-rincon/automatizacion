from django.contrib import admin
from .models import Task

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Custom Model admin.
    """
    list_display = ('id', 'title', 'description', 'completed')
    search_fields = ('id', 'title')
