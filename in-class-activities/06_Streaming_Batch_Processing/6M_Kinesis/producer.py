import boto3
import testdata
import json

kinesis = boto3.client('kinesis', region_name='us-east-1')

# Continuously write Twitter-like data into Kinesis stream
while True:
    test_tweet = {'username': testdata.get_username(),
                  'tweet':    testdata.get_ascii_words(280)}
    kinesis.put_record(StreamName="test_stream",
                       Data=json.dumps(test_tweet),
                       PartitionKey="partitionkey")
