# Amazon EC2

## Overview

Amazon Elastic Compute Cloud (Amazon EC2) provides scalable virtual servers for running applications in the cloud. In the DataShield platform, EC2 instances host the application services, archive server, and administration server, forming the core compute layer of the architecture.

---

# Purpose in DataShield

Amazon EC2 is used to:

- Host the Collector Service
- Host the Analyzer Service
- Host the Service Layer (Dashboard)
- Host the Archive Server
- Provide secure administration through the Bastion Host

Each instance performs a dedicated responsibility, following a microservices architecture.

---

# EC2 Instances

| Instance | Purpose | Access |
|-----------|----------|--------|
| Bastion | Secure administration | SSH / AWS Session Manager |
| Collector | Receives client requests | Private Subnet |
| Analyzer | Processes incoming data | Private Subnet |
| Service | Dashboard & Metadata API | Private Subnet |
| Archive | Encrypted NFS Storage | Private Subnet |

---

### Screenshot

![](screenshots/04-EC2/ec2-instances.png)

# Collector EC2

## Purpose

Acts as the entry point for incoming requests.

### Responsibilities

- Receive API requests
- Validate incoming data
- Store raw backups
- Forward requests to Analyzer

### Running Service

- FastAPI
- Uvicorn
- Systemd

### Listening Port

8080

### Screenshot

![](screenshots/08-Collector/collector-service.png)

![](screenshots/08-Collector/health-api.png)

---

# Analyzer EC2

## Purpose

Processes data received from the Collector.

### Responsibilities

- Analyze incoming data
- Generate processed JSON
- Upload files to Amazon S3
- Forward metadata

### Running Service

- FastAPI
- Uvicorn
- Systemd

### Listening Port

8081

### Screenshot

![](screenshots/09-Analyzer/api.png)

![](screenshots/09-Analyzer/analyzer-service.png)

---

# Service EC2

## Purpose

Provides the dashboard and metadata APIs.

### Responsibilities

- Store metadata in Amazon RDS
- Display processed files
- Serve dashboard
- Provide REST APIs

### Running Service

- FastAPI
- SQLAlchemy
- Uvicorn
- Systemd

### Listening Port

8000

### Screenshot

![](screenshots/10-Service/service-api.png)

![](screenshots/10-Service/metadata-api.png)

![](screenshots/21-dashboard/dashboard.png)

---

# Archive EC2

## Purpose

Provides secure backup storage.

### Responsibilities

- LUKS encrypted storage
- NFS server
- Raw backup storage

### Running Services

- NFS
- LUKS
- Systemd

### Screenshot

![](screenshots/11-Archive/lsblk.png)

![](screenshots/11-Archive/exports.png)

![](screenshots/11-Archive/filesys.png)

---

# Bastion Host

## Purpose

Acts as the secure administration server.

### Responsibilities

- SSH access
- Administrative tasks
- Secure entry point into private subnets


# Communication Flow

```
Internet
      │
      ▼
Application Load Balancer
      │
      ▼
Collector EC2
      │
      ▼
Analyzer EC2
      │
      ▼
Service EC2
      │
      ▼
Amazon RDS

Collector
      │
      ▼
Archive EC2
```

---

# Security

The EC2 instances follow several AWS security best practices:

- Private subnets for backend services
- Security Groups controlling network traffic
- IAM Roles instead of AWS access keys
- SSH restricted through the Bastion Host
- Communication over private IP addresses
- Encrypted storage using Amazon EBS and LUKS

---

# Monitoring

Each EC2 instance is monitored using:

- Amazon CloudWatch
- CloudWatch Agent
- Systemd service monitoring

---

# Advantages

- Independent microservices
- Easy horizontal scaling
- Secure deployment
- Flexible compute resources
- Simplified maintenance

---

# Key Takeaways

Amazon EC2 provides the compute foundation for the DataShield platform. Each application component runs on a dedicated EC2 instance, enabling isolation, scalability, and easier maintenance. This microservices-based deployment ensures that each service can be managed, monitored, and scaled independently while maintaining secure communication within the VPC.