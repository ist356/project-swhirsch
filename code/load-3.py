import os
import requests
from requests.auth import HTTPBasicAuth

def create_bucket(bucket_name, endpoint_url, access_key, secret_key):
    """Create a bucket in an S3-compatible service

    :param bucket_name: Bucket to create
    :param endpoint_url: Endpoint URL of the S3-compatible service
    :param access_key: Access key for authentication
    :param secret_key: Secret key for authentication
    :return: True if bucket was created, else False
    """
    url = f"{endpoint_url}/{bucket_name}"
    try:
        response = requests.put(url, auth=HTTPBasicAuth(access_key, secret_key))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("ERROR", e)
        return False
    return True

def upload_file(file_name, bucket_name, object_name=None):
    """Upload a file to an S3-compatible service

    :param file_name: Is a full path to the file to upload e.g. cache/file.csv 
    :param bucket_name: Bucket to upload to. this should be ist356yournetid
    :param object_name: S3 object name. this should be the file name without the cache/ prefix file.csv
    :return: True if file was uploaded, else False
    """
    # S3-compatible service configuration
    endpoint_url = 'https://play.min.io:9000'
    access_key = 'Q3AM3UQ867SPQQA43P2F'
    secret_key = 'zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG'

    # Create the bucket if it does not exist
    if not create_bucket(bucket_name, endpoint_url, access_key, secret_key):
        print(f"Failed to create bucket {bucket_name}")
        return False

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Construct the URL for the upload
    url = f"{endpoint_url}/{bucket_name}/{object_name}"

    # Read the file content
    with open(file_name, 'rb') as file:
        file_content = file.read()

    # Upload the file
    try:
        response = requests.put(url, data=file_content, auth=HTTPBasicAuth(access_key, secret_key))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("ERROR", e)
        return False
    return True

if __name__ == '__main__':
    # Load step: Upload the cleaned CSV file to the S3-compatible service
    file = 'Cache/cleaned_passing_data.csv'
    bucket = "ist356swhirsch"
    object_name = os.path.basename(file)
    success = upload_file(file, bucket, object_name)
    if success:
        print(f"File {file} uploaded successfully to bucket {bucket} as {object_name}")
    else:
        print(f"Failed to upload file {file} to bucket {bucket}")