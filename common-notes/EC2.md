# EC2 Notes

## EC2 - Elastic Compute Cloud

- ip address changes on restart
- use golden AMI to speed up startup
- restore EBS volumns from snapshots for speed

### Launch Types (Payment options)

- On Demand (linux by the second, Windows by the hour)
  - No long term commitments
  - Spiky, short term work loads
  - Development use
- Reserved (1 to 3 years in length)
  - Production servers
  - **Standard RI** up to 75% off on-demand costs
  - **Convertible RI** up to 54% off on-demand costs
  - **Scheduled RI** runs in a reserved time window (day, week, month)
- Spot (bid a price)
  - Run a low use times
  - Need high performance for a limited time
- Dedicated Hosts (Physical servers for you)
  - Regulatory needs
  - License needs
  - Can be hourly priced
  - Up to 75% off on-demand
  - It's your machine
- Dedicated Instances
  - multiple instances from same account can run on the same hardware
  - instance may move between hardware
  - no access or control over the physical hardware

### Instance Types

Check out https://EC2Instances.info

- **T2/T3** Lowest Cost, GP, burstable [development/testing]
- **T2/T3 Unlimited**, GP, infinite burst [development/testing]
- **M5** GP [Application Servers]
- **I3** High speed storage [DB]
- **G3** Graphics [Video Encoding/Streaming]
- H1 High disk throughput [MapReduce]
- D2 Dense Storage [Data Warehouse/Hadoop]
- F1 Field Programmable Gate Array [Analytics]
- **R4** Memory optimized [Memory Intensive/DB]
- **C5** Compute Optimized [CPU Intensive applications]
- P3 GPU [Machine Learning/Bit Coin Mining]
- X1 Memory Optimized (hugh amount of ram) [SAP/HANNA]

**FightDrMcPx** - remember instance types....

## Placement groups

- Cluster
  - grouped together for low latency network traffic
  - high speed network
  - same rack for the most part
- Spread
  - mininize failure risk, each ec2 instance is on different physical hardare (Limit to 7 instnaces per AZ placement group)
- Partition
  - Spread of Clusters in an AZ
  - up to 7 partitions
  - a partition is on a single rack, so ec2 instance in the partition share the same rack.

## EBS - Elastic Block Storage (attached volumes)

- Root device volume - boot and image drive
- EBS volume must be in same availablity zone as ec2 instance.
- create encrypted root volume by copying root volume and creating an ec2 image from the copied and encrypted root volume.

### Types of EBS

- GP2 General Purpose SSD
  - balance of price and performance
  - 3 IOPS per GB up to 10,000 IOPS with burst up to 3000 IOPS for volumes above 3334 GB
- Pervisioned IOPS SSD
  - Database use
  - Need more than 10,000 IOPS
- ST1 Throughput optimized HDD
  - cannot be boot volume
  - log files
  - big data
    SC1 - Cold HHD
  - cannot be boot volume
    Magnetic (Std)
  - legacy
  - can boot from

## AWS CLI

- stored in ~/.aws/config ~/.aws/credentials
- aws configure --profile {profile_name}
- export AWS_PROFILE={profile_name} or setx AWS_PROFILE {profile_name}

## Elastic IP

- can have max of 5 (can be increased)
- should not use unless required, use DNS or load balancer instead

## AMI - Amazon Machine Image

- can create custom images from existing snapshots
- created images are only in one region, can be copied to other regions
- can be private or public

### Cross acount sharing AMI

- can share with other accounts.
- cannot stop other from take ownership of the AMI.
- cannot copy a AMI with an associated billingProduct code, but you can create a new instance from the AMI.
- cannot copy an encrypted AMI, but can create a new instance from a snapshot.

## ASG - Auto scaling group

- ASG is free
- minimum size
- initial capacity
- actual size
- maximum size
- IAM roles attached to ASgG is assigned to all EC2 instances in the group

### Scaling Alarms

- can use CloudWatch alarms
- can scale in or out based on alarms
- can be based on (new rules):
  - target cpu average
  - requests per ELB
  - network in/out
- can create custom metric using CloudWatch (PutMetric API)

## Meta data

- URL is http://169.254.269.254/latest/meta-data
- can only be used from EC2 instance
