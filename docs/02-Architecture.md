The architecture consists of:

- API Gateway for exposing secure REST APIs.
- VPC Link connecting API Gateway to private resources.
- Application Load Balancer (ALB) for traffic distribution.
- Collector Service for receiving incoming requests.
- Archive Server for storing encrypted raw backups.
- Analyzer Service for processing incoming data.
- Amazon S3 for storing processed files.
- Service Layer for managing metadata.
- Amazon RDS for persistent metadata storage.
- CloudWatch and SNS for monitoring and alerting.
- Auto Scaling Group for high availability.

## 📖 Architecture Explanation

### 1. Client

The client sends a JSON request containing application data to the public API endpoint exposed through Amazon API Gateway.

### 2. Amazon API Gateway

API Gateway acts as the secure entry point into the application. It validates incoming requests and forwards them to resources inside the private VPC using VPC Link.

### 3. VPC Link

VPC Link provides secure connectivity between API Gateway and private AWS resources without exposing backend services directly to the internet.

### 4. Application Load Balancer

The Application Load Balancer distributes incoming traffic across backend application instances. It also performs health checks and works with Auto Scaling to improve application availability.

### 5. Collector Service

The Collector Service receives incoming requests through FastAPI.

Its responsibilities include:
- Validating incoming requests
- Creating raw backup files
- Writing raw files to the Archive Server
- Forwarding requests to the Analyzer Service

### 6. Archive Server

The Archive Server stores raw backup files.

Security is enhanced by:
- LUKS disk encryption
- NFS shared storage
- Dedicated encrypted EBS volume

### 7. Analyzer Service

The Analyzer Service processes incoming data received from the Collector Service.

After processing:
- Processed files are uploaded to Amazon S3.
- Metadata is sent to the Service Layer.

### 8. Amazon S3

Amazon S3 stores processed JSON files.

S3 provides:
- Durable object storage
- High availability
- Scalability
- Versioning support

### 9. Service Layer

The Service Layer receives metadata from the Analyzer Service and stores it in Amazon RDS. It also provides REST APIs used by the dashboard.

### 10. Amazon RDS

Amazon RDS stores metadata such as:
- Filename
- File size
- Upload timestamp

### 11. Monitoring

Amazon CloudWatch continuously monitors infrastructure metrics.

Amazon SNS sends email notifications whenever configured alarms are triggered.

### 12. Auto Scaling

Auto Scaling automatically launches replacement instances when required and maintains application availability.