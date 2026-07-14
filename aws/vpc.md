# Amazon VPC

## Overview

Amazon Virtual Private Cloud (VPC) provides an isolated and secure virtual network where all DataShield resources are deployed. It enables complete control over networking, routing, and communication between AWS resources while keeping backend services protected from direct internet access.

---

## Purpose in DataShield

The VPC acts as the foundation of the entire infrastructure by:

- Providing a private network for all resources
- Isolating application components from other AWS customers
- Enabling communication between EC2 instances
- Supporting public and private subnet architecture
- Allowing secure access through Internet Gateway and NAT Gateway

---

## Configuration

| Setting | Value |
|----------|-------|
| Region | ap-south-1 (Mumbai) |
| CIDR Block | 10.60.0.0/16 |
| DNS Resolution | Enabled |
| DNS Hostnames | Enabled |

---

## Architecture

The VPC contains:

- Public Subnets
- Private Application Subnets
- Private Database Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups

---

## Network Layout

```
Internet
    │
    ▼
Internet Gateway
    │
    ▼
──────────────────────────────────────────
           Amazon VPC
        10.60.0.0/16
──────────────────────────────────────────

Public Subnet
│
├── Bastion Host
├── Application Load Balancer
└── NAT Gateway

Private Subnets
│
├── Collector
├── Analyzer
├── Service
├── Archive
└── Amazon RDS
```
---

## Why Amazon VPC?

Amazon VPC was selected because it provides:

- Network isolation
- Secure communication
- Flexible subnet design
- Route table management
- Integration with AWS networking services
- Fine-grained security controls

---

## Benefits

- Secure architecture
- Private communication between services
- Controlled internet access
- Easy scalability
- High availability support

---

# Screenshots

## VPC Overview

![](screenshots/01-vpc/vpc.png)

---

## VPC Details

Show:

- VPC Name
- CIDR Block

## Key Takeaways

The Amazon VPC serves as the secure networking foundation of the DataShield platform. By isolating application components and separating public and private resources, it ensures secure communication while supporting scalable cloud infrastructure.