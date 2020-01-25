# Serverless

## Lambda

- computer service
- supported languages
  - NodeJS
  - Java
  - Python
  - C#
  - Go
  - Powershell
  - Ruby
- first 1 million requests per month are free, plus 400,000 GBs of compute time
- \$0.20 per next 1 million requests
- more memory, higher cost
- X-ray to debug ??
- limited to 1000 concurrent functions
- /tmp 512 MB of disk space
- limit to 50 MB package size (zipped)
- limit to 250 MB package size deployed
- environment max 4 KB
- triggers
  - API Gateway
  - IoT
  - Alexa Skills Kit
  - Alexa Smart Home
  - Application Load Balancer
  - CloudFront
  - CloudWatch
  - CloudWatch Logs
  - CodeCommit
  - Cognito Sync Trigger
  - DynamoDB
  - Kinesis
  - S3
  - SNS
  - SQS
- Qualified/Unqualified ARNs
  - no suffix is unqualified,
  - \$LATEST or alias (PROD/DEV/etc)
  - split traffic between 2 versions by percent (except \$LATEST)
  - cannot modify non \$LATEST versions

## Lambda@Edge

- think CDN for Lambda
- modify all requests/responses going through CloudFront
- uses
  - security
  - dynamic web application
  - SEO
  - routing
  - bot mitigation
  - image transform
  - A/B testing
  - authentication/authorization
  - prioritization
  - user tracking/analytics

## Serverless Services

- Lambda/Lambda@Edge
- S3
- EFS
- API Gateway
- RDS Aurora Serverless
- DynamoDB
- Fargate
- SNS
- SQS
- Step Functions
- AppSync
- EventBridge
- Kinesis
- Athena

## API Gateway

- can cache response for TTL seconds
- CORS (hot topic in test)
- Can import from a Swagger 2.0/3.0 file
- throttle to 10,000 rps (HTTP error 429)
  - limit can be changed, but will cost
  - per AWS account, NOT region or gateway
- max concurrent requests is 5000 per account (HTTP error 429)
  - limit can be changed, but will cost
  - per AWS account, NOT region or gateway
- can use as SOAP pass through

## Step Functions

- workflow orchestration with Amazon States Language (JSON)
- types of workflows
  - sequential
  - branching
  - parallel
- see jobs running the Batch
- clean up with delete of CloudFormation stack

## X-Ray

- SDK provides
  - interceptors
  - client handlers
  - HTTP client to instrument other services
