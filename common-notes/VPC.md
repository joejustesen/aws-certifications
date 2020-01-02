# VPC - Virtual Private Cloud

- allowed 5 per region per account
- needs a name and CIDR block /16 to /28

## Subnets

- make public by adding internet gateway (IGW)
- cannot use the first 4 and last address in a subnet
  - \*.\*.\*.0 is network
  - \*.\*.\*.1 is aws routing
  - \*.\*.\*.2 is aws dns
  - \*.\*.\*.3 is aws reserved
  - \*.\*.\*.255 is broadcast address

## NACLS - Network ACLS

- subnet firewalls
