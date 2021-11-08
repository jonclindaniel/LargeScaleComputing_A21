import boto3

session = boto3.Session()
kinesis = session.client('kinesis')

# Delete Kinesis Stream (if it currently exists):
try:
    response = kinesis.delete_stream(StreamName='test_stream')
except kinesis.exceptions.ResourceNotFoundException:
    pass # don't care why it doesn't exist -- just don't want to pay for it

# Confirm that Kinesis Stream was deleted:
waiter = kinesis.get_waiter('stream_not_exists')
waiter.wait(StreamName='test_stream')
print("Kinesis Stream Successfully Deleted")
