from django.db import models
from django.contrib.auth.models import User


class Todolist(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
