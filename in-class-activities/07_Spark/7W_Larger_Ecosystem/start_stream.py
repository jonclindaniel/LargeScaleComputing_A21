import boto3
import testdata
import json
import time

session = boto3.Session()
kinesis = session.client('kinesis')
ec2 = session.resource('ec2')
ec2_client = session.client('ec2')

response = kinesis.create_stream(StreamName='test_stream',
                                 ShardCount=1
                                )

# Is the stream active and ready to be written to/read from? Wait until it exists before moving on:
waiter = kinesis.get_waiter('stream_exists')
waiter.wait(StreamName='test_stream')
print("Kinesis Stream is ready")

# Continously write Twitter-like data into Kinesis stream
while True:
    test_tweet = {'username': testdata.get_username(),
                  'age': testdata.get_int(18, 100),
                  'num_followers': testdata.get_int(0, 10000),
                  'tweet':    testdata.get_ascii_words(280)
                  }
    kinesis.put_record(StreamName="test_stream",
                       Data=json.dumps(test_tweet),
                       PartitionKey="partitionkey"
                      )
