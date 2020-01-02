# Load Blancer

- can provide SSL termination
- can enforce cookie stickiness
- use SSL certificate stored in ACM (AWS Certificate Manager)
- can have multiple certs for multiple domain names
- clients can use SNI (Server Name Indication) to specify hostname they reach

## ELB EC2 Load Balancer

- integrated with AWS services
- all have static hostnames, do now use the underlying IP address
- will scale with load, but takes time
- check security groups if cannot connect to application

### CLB - Classic

- don't use (v1), deprecated
- privides health checks (port and a route) on http
- cannot load balance to multiple applications on same machine

### ALB - Application Load Balancer (v2)

- layer 7
- load balance to multiple applications on the same machine, think containers
- load balance on route in URL _or_ hostname in URL
- uses port mapping to redirect to dynamic port
- can be sticky
- supports HTTP/HTTPS/WebSockets
- cannot see client IP, check X-Forwarded-For/X-Forwared-Port/X-Forwarded-proto in header
- latency ~400ms
- 503 error -> at capacity or no matching target

### NLB - Network Load Balancer (v2)

- layer 4
- handles TCP traffic
- very high performance
- latency ~100ms
- can see client IP
- has static IP per AZ
- if public, must have an Elastic IP attached
- if private, will get same random IP at creation
- has cross zone balancing
- as SSL termination

### Stickiness

- client directed to same EC2 instance
- uses cookie with expire datetime

### Security Groups

- use sg attached to LB as source for internal EC2 sg to only allow traffic from LB to the EC2
- [Users] <- HTTPS -> [LB] <- HTTP / private VPC -> [EC2, EC2, EC2, EC2]
