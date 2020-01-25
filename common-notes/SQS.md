# SQS - Simple Queue Service

- producer sends messages
- consumer polls messages

## Types of Queues

### Standard Queue

- up to 10,000 message per second
- retention default 4 days, up to 14 days
- no limit to number of messages in a queue
- low latency < 10 ms
- delivery at least once (can have dups)
- can be out of order (best effort ordering)
- max 256KB of data per messages
- delay up to 15 minutes, default is 0 seconds

### FIFO Queue

- name must end in .fifo
- up to 300 messages per second
- in order
- exactly once
- content based deduplication using duplication ID, good for 5 mins, duplication ID is basically the MD5 hash of the message body
- supports message groups, tag on message

### Dead Letter Queue

- after X failures, message is copied to DLG
- failed receive policy can be set for 1 to 1000 failures

## Message Producer

- body is up to 256KB
- meta data
- delivery delay
- get back ID and MD5 has of the body

## Message Consumer

- polls for messages
- process message within visibility timeout
- can delete message with ID or handle
- visibility timeout, other consumers cannot see the message (0 to 12 hours, default 30s)
- can change visiblity timeout for a message

### Long polling

- wait for timeout (1 to 20s) or message available
- decreases number of api calls, lowers latency
- preferred method
- can be configured at the queue level or per call with WaitTimeSeconds
