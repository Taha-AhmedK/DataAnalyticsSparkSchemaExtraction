import pyspark.sql as p
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import *
import re
import json

@api_view(["POST"])
def extract_metadata_s3(request):
    KAFKA_DATA_TYPES = {
    'STRING': 'STRING',
    'INTEGER' : 'INT32',
    'LONG' : 'INT64',
    'DECIMAL' : 'FLOAT32',
    'DOUBLE' : 'FLOAT64',
    'DATE' : 'STRING',
    'DATETIME' : 'STRING',
    'TIMESTAMP' : 'STRING',
    'STRUCT' : 'STRUCT'
}
    serializer = ExtractMetadataS3(data=request.data)
    # Fetch a spark session
    if serializer.is_valid():
        data = serializer._validated_data    
        
        # Extracting all required variables from request
        name :str = data.get('name')
        metadata :dict =data.get('metadata')        
        access_key :str = data.get('access_key')
        secret_key :str = data.get('secret_key')
        bucket_name :str = data.get('bucket_name')
        folder_path :str = data.get('folder')
        spark = p.SparkSession \
                    .builder \
                    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk:1.12.639") \
                    .config("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem") \
                    .config("fs.s3a.access.key", access_key) \
                    .config("fs.s3a.secret.key", secret_key) \
                    .config('spark.hadoop.fs.s3a.path.style.access', True) \
                    .getOrCreate()
        
        df = spark.read.csv(f"s3a://{bucket_name}/{folder_path}/", header=True)


        # print(type(df.printSchema()))
        field_schemas = json.loads(df.schema.json().replace("nullable", "isOptional").replace("fields", "fieldSchemas"))
        field_schemas['fieldSchemas'] = {f'{x["name"]}' : {'type' : KAFKA_DATA_TYPES[x["type"].upper()], "isOptional" : x["isOptional"]} for x in field_schemas['fieldSchemas']}
        field_metadata = field_schemas['fieldSchemas'].keys()


        field_schemas['name'] = name
        field_schemas['type'] = field_schemas['type'].upper()

        key_name_node  = list(field_schemas["fieldSchemas"].keys())[0]
        key_name_node_details =field_schemas["fieldSchemas"][key_name_node] 
        key_schema = {
            "name": f"{name}",
            "type": "STRUCT",
            "isOptional": False,
            "fieldSchemas": {
                key_name_node: key_name_node_details
            }
        }
        formatted_fields = ";".join([f"{name}:{schema['type']}" for name, schema in field_schemas['fieldSchemas'].items()])
        
        if len(metadata) != 0:
            changes_current_metadata = [x for x in metadata.keys() if x not in field_metadata]
            changes_current_file = [x for x in field_schemas['fieldSchemas'].keys() if x not in metadata.keys()]

            return Response({"schema" : field_schemas,
                             "key_schema" : key_schema,
                               "metadata_differences" : changes_current_metadata,
                                 "file_schema_differences" : changes_current_file,
                                    "formatted_schema" : formatted_fields
                                 },status=200)
        
        else:

            return Response({"schema" : field_schemas,"key_schema" : key_schema,"formatted_schema" : formatted_fields},status=200)
    return Response(serializer.errors, status=500)   

@api_view(["POST"])
def extract_metadata(request):
    KAFKA_DATA_TYPES = {
    'STRING': 'STRING',
    'INTEGER' : 'INT32',
    'LONG' : 'INT64',
    'DECIMAL' : 'FLOAT32',
    'DOUBLE' : 'FLOAT64',
    'DATE' : 'STRING',
    'DATETIME' : 'STRING',
    'TIMESTAMP' : 'STRING',
    'STRUCT' : 'STRUCT'
}
    serializer = ExtractMetadata(data=request.data)
    # Fetch a spark session
    spark : p.SparkSession = p.SparkSession.builder.appName("metadata-extractor").getOrCreate()
    if serializer.is_valid():
        data = serializer._validated_data    
        
        # Extracting all required variables from request
        name :str = data.get('name')
        file_location :str = data.get('file_location')
        metadata :dict =data.get('metadata')        
        
        df :p.DataFrame= spark.read.csv(file_location, header=True, inferSchema=True)

        # print(type(df.printSchema()))
        field_schemas = json.loads(df.schema.json().replace("nullable", "isOptional").replace("fields", "fieldSchemas"))
        field_schemas['fieldSchemas'] = {f'{x["name"]}' : {'type' : KAFKA_DATA_TYPES[x["type"].upper()], "isOptional" : x["isOptional"]} for x in field_schemas['fieldSchemas']}
        field_metadata = field_schemas['fieldSchemas'].keys()


        field_schemas['name'] = name
        field_schemas['type'] = field_schemas['type'].upper()

        key_name_node  = list(field_schemas["fieldSchemas"].keys())[0]
        key_name_node_details =field_schemas["fieldSchemas"][key_name_node] 
        key_schema = {
            "name": f"{name}",
            "type": "STRUCT",
            "isOptional": False,
            "fieldSchemas": {
                key_name_node: key_name_node_details
            }
        }
        if len(metadata) != 0:
            changes_current_metadata = [x for x in metadata.keys() if x not in field_metadata]
            changes_current_file = [x for x in field_schemas['fieldSchemas'].keys() if x not in metadata.keys()]

            return Response({"schema" : field_schemas,"key_schema" : key_schema, "metadata_differences" : changes_current_metadata, "file_schema_differences" : changes_current_file},status=200)
        
        else:

            return Response({"schema" : field_schemas,"key_schema" : key_schema},status=200)
    return Response(serializer.errors, status=500)        

