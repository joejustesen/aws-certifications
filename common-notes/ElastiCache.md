# ElastiCache

- in memory key-value store
- RDS caching
- shared state, like session data
- has pub/sub
- multi AZ failover
- cache survices reboots
- read replicas
- clustered

## Patterns

- lazy loading
- write through
- TTL - time to live for cached data
- session store

## Security

- does NOT support IAM
- SSL
- RedisAUTH

# Memcached

- does not surive reboots
- in memory key-value store

## Security

- does NOT support IAM
- supports SASL
