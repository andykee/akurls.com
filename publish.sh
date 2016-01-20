#!/bin/bash

S3_BUCKET_NAME="akurls.com"
S3_BUCKET_REGION="us-west-2"
LAMBDA_FUNCTION_NAME="akurls"

aws s3 ls s3://$S3_BUCKET_NAME --region $S3_BUCKET_REGION

