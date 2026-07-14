# Amazon Security Groups

## Overview

Amazon Security Groups act as stateful virtual firewalls that control inbound and outbound traffic for AWS resources. In the DataShield platform, Security Groups ensure that only authorized components communicate with each other while protecting backend services from direct public access.

---

# Purpose in DataShield

Security Groups were configured to:

- Secure communication between application components
- Restrict unnecessary network access
- Protect backend resources
- Follow the Principle of Least Privilege
- Control traffic between EC2 instances and Amazon RDS

---

# Security Groups Used

| Security Group | Attached Resource | Purpose |
|---------------|-------------------|---------|
| ALB-SG | Application Load Balancer | Accept client HTTP/HTTPS requests |
| Collector-SG | Collector EC2 | Receive requests from ALB |
| Analyzer-SG | Analyzer EC2 | Receive requests from Collector |
| Service-SG | Service EC2 | Dashboard and Metadata Service |
| Archive-SG | Archive EC2 | NFS Archive Storage |
| RDS-SG | Amazon RDS | MySQL Database |

---

# ALB Security Group

## Purpose

The Application Load Balancer receives incoming client traffic and forwards requests to the Collector Service.

### Inbound Rules

| Port | Protocol | Source |
|------|----------|--------|
| 80 | HTTP | 0.0.0.0/0 |
| 443 | HTTPS | 0.0.0.0/0 |

### Outbound Rules

All Traffic

### Screenshot

![](screenshots/06-SecurityGroups/alb-sg.png)

---

# Collector Security Group

## Purpose

Receives traffic only from the Application Load Balancer.

### Inbound Rules

| Port | Protocol | Source |
|------|----------|--------|
| 8080 | TCP | ALB Security Group |
| 22 | TCP | Bastion Security Group |

### Outbound Rules

| Port | Destination |
|------|-------------|
| 443 | Internet (AWS Services) |
| 8081 | Analyzer Security Group |
| 2049 | Archive Security Group |

### Screenshot

![](screenshots/06-SecurityGroups/collector-sg.png)

---

# Analyzer Security Group

## Purpose

Processes requests received from the Collector Service.

### Inbound Rules

| Port | Protocol | Source |
|------|----------|--------|
| ICMP | ICMP | VPC CIDR |
| 8081 | TCP | Collector Security Group |
| 22 | TCP | Bastion Security Group |

### Outbound Rules

| Port | Destination |
|------|-------------|
| 443 | Internet (AWS Services) |
| 8000 | Service Security Group |

### Screenshot

![](screenshots/06-SecurityGroups/analyzer-sg.png)

---

# Service Security Group

## Purpose

Hosts the dashboard and communicates with Amazon RDS.

### Inbound Rules

| Port | Protocol | Source |
|------|----------|--------|
| 8000 | TCP | Analyzer Security Group |
| 8000 | TCP | ALB Security Group |
| 80 | TCP | ALB Security Group |
| 22 | TCP | Bastion Security Group |

### Outbound Rules

| Port | Destination |
|------|-------------|
| 3306 | Amazon RDS |
| 443 | Internet (AWS Services) |

### Screenshot

![](screenshots/06-SecurityGroups/service-sg.png)

---

# Archive Security Group

## Purpose

Stores encrypted backups and shares them using NFS.

### Inbound Rules

| Port | Protocol | Source |
|------|----------|--------|
| 2049 | TCP | VPC CIDR (10.60.0.0/16) |
| 22 | TCP | Bastion Security Group |

### Outbound Rules

All Traffic

### Screenshot

![](screenshots/06-SecurityGroups/archive-sg.png)

---

# Amazon RDS Security Group

## Purpose

Protects the MySQL database by allowing connections only from authorized application servers.

### Inbound Rules

| Port | Protocol | Source |
|------|----------|--------|
| 3306 | TCP | Service Security Group |
| 3306 | TCP | Additional EC2 Security Group (Database Access) |

### Outbound Rules

Default

### Screenshot

![](screenshots/06-SecurityGroups/rds-sg.png)

---

# Security Flow

```
Internet
      │
      ▼
Application Load Balancer
      │
      ▼
Collector (8080)
      │
      ▼
Analyzer (8081)
      │
      ▼
Service (8000)
      │
      ▼
Amazon RDS (3306)

Collector
      │
      ▼
Archive Server (NFS - 2049)
```

---

# Why Security Groups?

Security Groups provide:

- Stateful packet filtering
- Resource-level security
- Automatic response traffic handling
- Easy rule management
- Fine-grained access control

---

# Best Practices Followed

- Backend services deployed in private subnets
- Only required ports exposed
- Database isolated behind its own Security Group
- SSH access restricted through the Bastion Host
- Security Group references used instead of public IP addresses wherever possible
- Least Privilege principle followed

---

# Key Takeaways

Security Groups form the primary network security layer of the DataShield platform. They ensure that each component communicates only with the services it requires, minimizing the attack surface while maintaining secure and efficient application communication.