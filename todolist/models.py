from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    todouser = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者
    todothing = models.CharField(max_length=50)
    tododone = models.BooleanField(default=False)
    todoworktime = models.IntegerField(default=0)
    todogshm = models.CharField(max_length=15)
