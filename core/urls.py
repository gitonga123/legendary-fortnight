from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploaded-statements', views.UploadLists.as_view(), name="statements"),
    path('upload-statement', views.UploadStatement.as_view(), name="upload_statement"),
    path('analyze-statement/<int:pk>', views.analyzePdf, name="statement_analysis")
]
