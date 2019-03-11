from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','todouser', 'todothing','tododone','todoworktime','todogshm')
