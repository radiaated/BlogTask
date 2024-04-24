from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField(max_length=5000, null=False, blank=False)
    created_date =  models.DateField(auto_now_add=True, null=False, blank=False)
    updated_date = models.DateField(auto_now_add=True, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title