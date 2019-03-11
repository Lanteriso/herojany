from django.contrib import admin
from .models import Todo

# Register your models here.

@admin.register(Todo)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', '用户','thing','done','work_time','格式化秒')