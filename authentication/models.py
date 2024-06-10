from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomerUser(AbstractUser):
    pass

class Blog(models.Model):
    author = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
