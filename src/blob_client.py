import os

# Import the client object from the SDK library
from azure.storage.blob import BlobClient

conn_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
container_name = os.environ["AZURE_CONTAINER_NAME"]

def get_blob_client(blob_name: str) -> BlobClient:
    return BlobClient.from_connection_string(conn_string, 
    container_name, blob_name)