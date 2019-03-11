from django.contrib import admin
from .models import Todo

# Register your models here.

@admin.register(Todo)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'todouser','thing','done','work_time','gshm')