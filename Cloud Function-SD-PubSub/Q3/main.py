import base64
import json
from google.cloud import storage

def storekr_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    pubsub_message = eval(pubsub_message)
    
    #read the messsage
    filename = pubsub_message['name'] + '.json'
    filecontent = eval(pubsub_message['content'])
    bucket_dest = filecontent['destination']
    
    #initialize storage client
    storage_client = storage.Client()
    bucket = None
    
    #get the bucket else create one
    try:
        bucket = storage_client.create_bucket(bucket_dest)
    except Exception as e:
        bucket = storage_client.get_bucket(bucket_dest)
    
    #upload the file to bucket
    blob = bucket.blob(filename)
    blob.upload_from_string(json.dumps(filecontent, indent = 4,sort_keys = True))
