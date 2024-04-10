import pandas as pd
from google.cloud import storage
import time

def overwrite_csv_to_gcs(local_csv_path, bucket_name, blob_name):
    # Read the local CSV file
    df = pd.read_csv(local_csv_path)

    # Create a client
    client = storage.Client()
    # Get the bucket
    bucket = client.get_bucket(bucket_name)

    # Get the blob
    blob = bucket.blob(blob_name)

    # Overwrite the CSV file to Google Cloud Storage
    blob.upload_from_filename(local_csv_path)

# Call the function to read the local CSV file and overwrite it to Google Cloud Storage
# Please replace 'local_csv_path', 'bucket_name', and 'blob_name' with your actual values
while True:
    overwrite_csv_to_gcs("C:\\Users\\ADMIN\\Desktop\\python\\coinprices.csv", 'coins_bket', 'coinprices.csv')
    print("The local CSV file was successfully read and overwritten to Google Cloud Storage.")
    time.sleep(5)