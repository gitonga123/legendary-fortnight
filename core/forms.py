from django import forms
from .models import FileStatements


from django import forms
from .models import FileStatements  # Import your model here


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileStatements
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file_uploaded': forms.FileInput(attrs={'class': 'form-control custom-file-input'}),
            'year': forms.NumberInput(attrs={'class': 'form-control custom-file-input'}),
        }
