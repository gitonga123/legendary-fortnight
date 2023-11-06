from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import FileStatements
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UploadFileForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UploadLists(ListView):
    model = FileStatements
    template_name = "uploaded_statements.html"

class UploadStatement(CreateView):
    model = FileStatements
    template_name = "new_statement.html"

    form_class=UploadFileForm
    success_url = reverse_lazy("statements")


    def form_valid(self, form):
        form.instance.user = self.request
        messages.success(self.request, 'The file was uploaded successfully')

        return super(UploadStatement, self).form_valid(form)