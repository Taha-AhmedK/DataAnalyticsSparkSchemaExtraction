# serializers.py
from rest_framework import serializers


class ExtractMetadata(serializers.Serializer):
    name=serializers.CharField()
    file_location = serializers.CharField()
    metadata = serializers.JSONField()

class ExtractMetadataS3(serializers.Serializer):
    access_key=serializers.CharField()
    secret_key=serializers.CharField()
    bucket_name=serializers.CharField()
    folder=serializers.CharField()
    name=serializers.CharField()
    metadata = serializers.JSONField()
    
