# ☁ AWS Infrastructure Documentation

This folder contains detailed documentation for every AWS service used in the DataShield project.

## AWS Services

| Service | Description |
|---------|-------------|
| 🌐 [VPC](vpc.md) | Virtual Private Cloud configuration |
| 🛣️ [Subnets & Networking](subnets.md) | Public/private subnets, Route Tables, NAT Gateway, Internet Gateway |
| 🔒 [Security Groups](security-groups.md) | Inbound and outbound access rules |
| 👤 [IAM](iam.md) | IAM Roles and permissions |
| 🖥️ [EC2 Infrastructure](ec2.md) | Collector, Analyzer, Service, Archive and Bastion instances |
| ⚖️ [Application Load Balancer](alb.md) | ALB configuration and listeners |
| 📈 [Auto Scaling Group](asg.md) | Automatic scaling and recovery |
| 🌍 [API Gateway & VPC Link](api-gateway.md) | Public API integration with private resources |
| 🪣 [Amazon S3](s3.md) | Object storage configuration |
| 🗄️ [Amazon RDS](rds.md) | MySQL database configuration |
| 📊 [CloudWatch](cloudwatch.md) | Monitoring and logging |
| 🔔 [Amazon SNS](sns.md) | Alert notifications |

---

## Architecture

The following diagram illustrates how these AWS services work together.

![](assets/architecture.png)