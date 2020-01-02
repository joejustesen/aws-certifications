# Route 53 - DNS service

- public nmaes, domain names you own
- private names, resolves to instances in your VPC
- can load balance
- health checks
- routing policy
  - simple
    - map domain to URL
    - cannot attach health check
    - can return multiple values
    - used for client side load balancing
  - failover
    - primary location, uses health check
    - secondary location.
  - geolocation
    - must provide a default route
    - route by country or continent
  - latency
    - most useful, routed to least latency
  - weighted
    - percent routed by weights
    - can use health checks
  - multi value
    - improved simple routing,
    - allow health checks
    - up to 8 multiple values returned
- costs \$0.50 per month per hosted zone

### Health Checks

- unhealthy, default is 3 failures
- healthy, default is 3 passed
- default interval is 30 seconds per health checker
- AWS launches 15 health checkers per health check
  - so the defaul tis one request every 2 seconds
- can be HTTP, TCP, HTTPS
- can be linked to Route53 DNS
- can be:
  - endpoint.
  - other health checks
  - Cloudwatch Alarm
- fast health checks, every 10 seconds, but costs more

### Record types

- A: URL to IPv4
- AAAA: URL to IPv6
- CNAME: URL to URL
  - non-root domains only
- Alias: URL to AWS resource
  - can be root domains
  - free of charge
  - has native health checks

### Use 3rd party registrar

- create hosted zone in Route 53
- update NS records on 3rd party website to use Route 53 DNS
