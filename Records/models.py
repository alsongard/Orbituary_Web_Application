from django.db import models

# Create your models here.
class Record(models.Model):
    first_name = models.CharField(max_length=35)
    middle_name = models.CharField(max_length=35, null=True, blank=True)
    last_name = models.CharField(max_length=35)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
