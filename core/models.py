from django.db import models

# Create your models here.
class FileStatements(models.Model):
    title = models.CharField(max_length=200)
    file_uploaded = models.FileField()
    year = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at', '-year']
        verbose_name = 'File Statement'
        verbose_name_plural = 'File Statements'
    

    def __str__(self) -> str:
        return self.title