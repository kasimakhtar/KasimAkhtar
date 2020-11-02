This function intregrates AWS S3, AWS Lambda and AWS SNS, to send an SMS with the word count of a text file. Uploading the file triggers the lambda function. The function counts the words and creates an SNS topic, which includes a message stating the word count of the file. This code incorporates [Emre Yilmaz's code](https://blog.shikisoft.com/send-sms-with-sns-aws-lambda-python/) with aspects of [Chirag Rathod's code](https://github.com/srcecde/aws-tutorial-code/blob/master/lambda/lambda_read_file_s3_trigger.py).


~~~

import boto3
import logging


# Initialize logger and set log level
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize SNS client for region
session = boto3.Session(
    region_name="us-east-1"
)
sns_client = session.client('sns')


def lambda_handler(event, context):
    # word count file from s3    
    word_count = 0
    s3 = boto3.client("s3")
    if event:
        file_obj = event["Records"][0]
        bucketname = str(file_obj['s3']['bucket']['name'])
        filename = str(file_obj['s3']['object']['key'])
        fileObj = s3.get_object(Bucket=bucketname, Key=filename)    
        for line in fileObj:
            word_count += len(line.split())
    # Send message
    response = sns_client.publish(
        PhoneNumber= "+447392248644",
        Message = "The word count in the file" + filename + " is " + str(word_count) + " .",
        MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': 'SENDERID'
            },
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Promotional'
            }
        }
    )

    logger.info(response)
    return 'OK'

~~~

NOTE: 

* In order for the function to work, AWS Lambda needs the following permissions:
 
  * AWSLambdaBasicExecutionRole
  * AmazonSNSFullAccess
  * AmazonS3FullAccess

* The function has S3 as a trigger but not SNS as a destination, the function includes code for SNS instead..
