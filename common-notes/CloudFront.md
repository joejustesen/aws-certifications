# CloudFront

- max TTL 31536000 seconds (365 days)
- default TTL 86400 seconds (24hrs)
- protect content with signed URLs or signed cookies
- WAF projects you at the application layer, automatically projects you from DOS
- SSL cert, can bring your own and store in ACM or IAM
- can be used in front of EC2 and ALB
- supports RTMP Protocol (video/media)

### Signed URLs

- use [OAI](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) to restrict access to S3 content
- use AWS SDK to generate

### Geo Restrictions

- white listed
- black listed
- determined from Geo-IP database
