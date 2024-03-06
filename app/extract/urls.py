from django.urls import path
from .views import *

urlpatterns = [
    path('extract-schema',extract_metadata,name='extract-schema'),
]