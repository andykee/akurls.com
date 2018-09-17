# akurls.com
akurls is a link aggregator that is specifically designed to cut down on the consumption of web content. You are forced to choose between seeing the most recent 10 or 30 articles from a site. Once it't no longer in the top 10 (or 30), it's gone. akurls runs on AWS Lambda and S3

1. Make sure Python 3.x is installed:

   which python3
   
2. Install pip3:

   sudo apt-get update
   sudo apt-get install pip3
   
3. Install akurls.com

   pip install git+http://github.com/andykee/akurls.com --user




## Installation
1. Download the akurls source. Create a virtualenv, activate it, and install all dependencies by running `pip install -r requirements.txt`.

2. [Set up a static website using a custom domain](http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) Make a note of the region you create your S3 buckets in - your Lambda region will need to match this later.

3. Configure akurls to point to the correct S3 bucket. This is done by setting `S3_BUCKET` in config.py. This should be the `<url>.com` bucket created in step 2 (not the `www.<url>.com` bucket).

4. Create an AWS IAM Execution Role so that the Lambda function can write to S3:

    * From the AWS console, select *Identity & Access Management*

    * Select *Roles*

    * Select *Create New Role*

        * Role Name: `lambda_s3_execution`

        * Role Type: AWS Lambda

        * Attach the following policies: `AmazonS3FullAccess` and `AWSLambdaExecute`

        * Select *Create Role*

5. Create an AWS Lambda deployment package by running `makedp.sh`.

6. Create an AWS Lambda function:

    * From the AWS console, select *Lambda*

    * Select *Create a Lambda function*

    * Skip blueprint selection

    * Configure the function with the following settings and then select *Next*:

        * Name: akurls
        * Description: akurls Lambda function
        * Runtime: Python 2.7
        * Lambda function code: upload zip created by running `makedp`
        * Handler: akurls.app
        * Role: `lambda_s3_execution`
        * Timeout: 30 sec

7. Configure a [Scheduled Event](http://docs.aws.amazon.com/lambda/latest/dg/with-scheduled-events.html) to initiate the Lambda Function

