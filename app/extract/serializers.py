# serializers.py
from rest_framework import serializers


class ExtractMetadata(serializers.Serializer):
    name=serializers.CharField()
    file_location = serializers.CharField()
    metadata = serializers.JSONField()

    
