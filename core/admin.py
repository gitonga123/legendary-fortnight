from django.contrib import admin
from .models import FileStatements

# Register your models here.
class FileStatementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'created_at')
    list_filter = ('year', 'title')

admin.site.register(FileStatements, FileStatementsAdmin)