## 🚀 Deployment Guide

### Prerequisites

Before deploying DataShield, ensure the following requirements are met:

- AWS Account
- Amazon Linux 2023 EC2 Instances
- AWS CLI configured
- Python 3.9+
- Git
- FastAPI
- Uvicorn
- MySQL Client
- IAM Roles with required permissions

### Step 1: Create Networking

- Create a custom Amazon VPC.
- Create public and private subnets.
- Attach an Internet Gateway.
- Configure a NAT Gateway.
- Configure Route Tables.
- Configure Security Groups for each application tier.

### Step 2: Launch EC2 Instances

Deploy the following EC2 instances:

- Bastion Host
- Collector Server
- Analyzer Server
- Service Server
- Archive Server

Assign appropriate IAM Roles and Security Groups.

### Step 3: Configure Archive Server

- Attach an additional Amazon EBS volume.
- Encrypt the volume using LUKS.
- Create an ext4 filesystem.
- Mount the encrypted filesystem.
- Configure NFS Server.
- Export the archive directory.

### Step 4: Configure Collector

- Install Python dependencies.
- Deploy the FastAPI application.
- Mount the Archive NFS share.
- Configure the Collector systemd service.
- Verify the Collector health endpoint.

### Step 5: Configure Analyzer

- Install required Python packages.
- Configure Amazon S3 access using IAM Roles.
- Deploy the Analyzer FastAPI service.
- Configure communication with the Service layer.

### Step 6: Configure Service Layer

- Install Python dependencies.
- Configure Amazon RDS connection.
- Deploy the FastAPI dashboard.
- Verify metadata storage.

### Step 7: Configure AWS Services

- Amazon S3 Bucket
- Amazon RDS
- IAM Roles
- CloudWatch
- SNS
- Application Load Balancer
- Launch Template
- Auto Scaling Group
- API Gateway
- VPC Link

### Step 8: Validate Deployment

Verify:

- Collector Service
- Analyzer Service
- Service Layer
- Archive Storage
- Amazon S3 Uploads
- Amazon RDS Entries
- CloudWatch Metrics
- SNS Notifications
- API Gateway Endpoint