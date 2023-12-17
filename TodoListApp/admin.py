from django.contrib import admin
from .models import TodoListModel


@admin.register(TodoListModel)
class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'dueDate', 'status', 'timestamp', 'tags')
    list_filter = ('status', 'timestamp')
    search_fields = ('title', 'description')
    readonly_fields = ('timestamp',)
