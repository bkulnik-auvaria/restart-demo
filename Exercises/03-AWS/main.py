import boto3


session = boto3.Session(
    aws_access_key_id="....",  # <---- setup the key here or create a profile
    aws_secret_access_key="....",
    region_name="eu-central-1"
)
# object of type session

s3client = session.client("s3")  # object of type "s3client"

s3_get_object_response = s3client.get_object(
    Bucket="restart-bucket-1234839934",
    Key="hello.txt"
)


if s3_get_object_response["ResponseMetadata"]["HTTPStatusCode"] != 200:
    print("get_object() failed")
    exit(-1)


# s3_get_object_response["Body"]  === type of StreamingBody
# open("file.txt") <-- file stream

# Everything is a file in Unix/Linux

content = s3_get_object_response["Body"].read()

print(content)