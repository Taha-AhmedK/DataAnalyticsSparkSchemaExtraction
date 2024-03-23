from django.urls import path
from .views import *

urlpatterns = [
    path('extract-schema',extract_metadata,name='extract-schema'),
    path('extract-schema-s3',extract_metadata_s3,name='extract-schema-s3')
]