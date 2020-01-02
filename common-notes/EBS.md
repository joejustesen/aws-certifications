# Elastic Block Storage

- tied to an AZ, can move snapshot between AZ
- provision with GBs & IOPS
- billed on capacity not use
- can increase capacity as needed

### Types

- GP2 (SSD) general purpose **bootable**
  - 1GB to 16TB, burst 3000 IOPS, max 16,000 IOPS
  - 3 IOPS per GB
- IO1 (SSD) highest performance **bootable**
  - 4GB to 16TB, 100 to 32,000 IOPS (nitro 64,000 IOPS)
  - 50 IOPS per GB
- STI (HDD) high through put, big data
  - not bootable
  - 500GB to 16TB
  - max 500 IOPS
  - 40MB/TB, max throughput 500MB/sec, can burst
- SCI (HDD) low cost, less frequently accessed
  - not bootable
  - 500GB to 16TB
  - max 250 IOPS
  - 12MB/TB, max throughput 250MB/sec, can burst

### Snapshot

- stored in S3, charges apply
- uses IOPS
- max 100,000 snapshots
- can copy between AZ/REGIONS
- can make AMI fron snapshot
- EBS volumes restored need to be pre-warmed (fio or dd command)
- can use Amazon Data Lifecycle Manager
