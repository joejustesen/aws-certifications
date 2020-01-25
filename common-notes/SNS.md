# SNS - Simple Notification Service

Send one message to many receivers.

- Subscribers can be:
  - SMS
  - email
  - SQS
  - HTTP/HTTPS endpoint
  - lambda function
  - Mobile Notifications
- pub/sub model, up to 10,000,000 subscriptions per topic
- topics (100,000 limit)
  - multiple subscribers
  - stored redundantly
- pay as you go,
  - \$0.50 per 1 million requests
  - \$0.06 per 100,000 HTTP notifications
  - \$0.75 per 100 SMS notifications
  - \$2.00 per 100,000 emails

### Topic Publish

- create topic
- create subscription
- publish to topic

### Direct Publish (mobile SDK)

- create platform application
- create platform endpoint
- publish to plateform endpoint

## SNS + SQS: Fan Out

- push SNS, many SQS queues subscribed
