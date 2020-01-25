# Other

## Cognito

Provides identity to users

- User Pools (CUP)
  - sign in functionality for app users (username/password, mfa)
  - can enable federated identies from (Facebook, Google, SAML)
  - sends back JWT
  - integrated with API Gateway
- Identity Pools (federated identity)
  - provides AWS temporary credentials for users to access AWS resources directly
  - integrated with user pools
- Sync
  - sync data it

## SES - Simple Email Service

- pay as you go
- can receive emails delivered to S3 bucket
- incoming emails can trigger lambda or SNS notifications

## Systems Manager Parameter Store

- versioned key value store
- standard
  - up to 10,000 parameters
  - 4 KB max values size
- advanced
  - more than 10,000 parameters
  - 8 KB max values size
- value types
  - String
  - StringList
  - SecureString
    - Encrypt using KMS key

## CLI

- never use credentials on EC2, use IAM roles

## Amazon MQ

For migration of existing messaging infrastructure to the cloud

- managed Apache ActiveMQ
- runs on dedicated machine, but can be HA with failover
- protocols: MQTT, AMQT, STOMP, Openwire, WSS

## API Gateway

- handles api versioning
- different environments
- handles authenticates and authorizatoin
- limit via api keys, request throttling
- intergration with Swagger/OpenAPI
- can cache responses
- security
  - IAM permissions (with Sig v4)
  - Lambda Authorizer returns IAM policy (or called Customer Authorizer)
    - check token in header
    - used for OAuth/SAML
  - Cognito User Pools
    - authentication, does not support authorization

### Outside VPC

- AWS Lambda
- EC2 endpoints
- load balancers
- any aws service
- any external http endpoints

### Inside VPC

- AWS Lambda
- EC2 endpoints
