from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import FileStatements
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UploadFileForm
from .services import extract_data_content
import os
from django.conf import settings


def index(request):
    return render(request, 'index.html', {})


def analyzePdf(request, pk):
    statement = FileStatements.objects.get(pk=pk, processed=False)
    filepath = os.path.join(settings.MEDIA_ROOT, statement.file_uploaded.name)
    extract_data_content(filepath, statement.year)
    return render(request, 'analyze.html', {"statement": statement})


class UploadLists(ListView):
    model = FileStatements
    template_name = "uploaded_statements.html"
    context_object_name = 'statements'
    paginate_by = 10


class UploadStatement(CreateView):
    model = FileStatements
    template_name = "new_statement.html"

    form_class = UploadFileForm
    success_url = reverse_lazy("statements")

    def form_valid(self, form):
        form.instance.user = self.request
        messages.success(self.request, 'The file was uploaded successfully')

        return super(UploadStatement, self).form_valid(form)
