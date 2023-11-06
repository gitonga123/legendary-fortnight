from django.db import models

# Create your models here.
class FileStatements(models.Model):
    title = models.CharField(max_length=200)
    file_uploaded = models.FileField()