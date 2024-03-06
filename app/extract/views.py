import pyspark.sql as p
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import *
import re
import json



@api_view(["POST"])
def extract_metadata(request):
    KAFKA_DATA_TYPES = {
    'STRING': 'STRING',
    'INTEGER' : 'INT32',
    'LONG' : 'INT64',
    'DECIMAL' : 'FLOAT32',
    'DOUBLE' : 'FLOAT64',
    'DATE' : 'org.apache.kafka.connect.data.Date',
    'DATETIME' : 'org.apache.kafka.connect.data.Timestamp',
    'TIMESTAMP' : 'org.apache.kafka.connect.data.Timestamp',
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
        field_schemas['fieldSchemas'] = {f'{sanitize_string(x["name"])}' : {'type' : KAFKA_DATA_TYPES[x["type"].upper()], "isOptional" : x["isOptional"]} for x in field_schemas['fieldSchemas']}
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


def sanitize_string(input_string):
    '''
        This method is being used to sanititze the field names 
        when generating fieldSchemas for kafka connect implementation

        sanitized_string contains : only letters [A-Z][a-z][0-9] and _
        any special characters are replaced with _
        _'s appearing more than once are replaced with only one _ 
        leading and traling _ are removed from string.
    '''

    sanitized_string = re.sub(r'[^\w]', '_', input_string)
    
    sanitized_string = re.sub(r'_{2,}', '_', sanitized_string)
    
    sanitized_string = sanitized_string.strip('_')
    
    return sanitized_string