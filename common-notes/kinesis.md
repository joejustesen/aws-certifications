# Kinesis

- streaming data service
- load and analyze stream data

## Costs

- hourly shard cost
- put cost per 25KB of data added to the stream
- extra
  - extended data retention
  - enhanced fanout

## Types of streams

### Video

- not covered ??

### Streams

- store for 24 hours (default) up to 7 days
  - can be replayed
- stored in shards, move shards, more throughput
- consumers
  - EC2, Lambda, EMR, Kinesis Data Analytics
  - multiple consumers can consome the same stream
- a single shard
  - cost is per shard
  - reads 5 TPS, up to 2 MB per second
  - writes 1000 TPS, up to 1 MB per second
  - 10 shards limited per region
  - records are ordered per shard
  - resharding is adding/removing shards
- data key hashed is the shard key, same key, same key
- use batching to to reduce cost
- use retry w/backoff on overload of shard

### Firehose

- automated streams
- no data retention
- data sent to S3 or Elasticsearch Cluster
- near real time (60 second latency)
- pay for data processed only

### Analytics

- auto scaling
- SQL queries of dta
- store query results into S3, RedShift, Elasticsearch Cluster
- pay per consumption

## Security

- IAM Policys
- encrypted at rest with KMS
- HTTPS endpoints
