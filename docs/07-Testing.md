# Testing and Validation

## Overview

The DataShield platform was tested component by component and finally validated using end-to-end integration testing.

---

# 1. Collector Service

## Objective

Verify that the Collector receives requests and forwards them correctly.

### Command

```bash
curl -X POST http://localhost:8080/collect \
-H "Content-Type: application/json" \
-d '{"filename":"sample.json","size":123}'
```

### Expected Result

- HTTP 200 OK
- Request forwarded to Analyzer
- Raw backup created.

---

# 2. Analyzer Service

## Objective

Verify that the Analyzer processes requests.

### Command

```bash
curl -X POST http://localhost:8081/analyze \
-H "Content-Type: application/json" \
-d '{"filename":"sample.json","size":123}'
```

### Expected Result

- Processed JSON generated
- Uploaded to Amazon S3

---

# 3. Archive Server

## Objective

Verify encrypted NFS storage.

### Test

Create a file from Collector:

```bash
echo test > /archive-backups/test.txt
```

Verify on Archive:

```bash
cat /archive-backups/test.txt
```

### Expected Result

The file is immediately visible on the Archive server.

---

# 4. LUKS Encryption

Objective

Verify encrypted EBS volume.

Command

```bash
lsblk -f
```

Expected

Encrypted LUKS volume mounted.

---

# 5. Amazon S3

Objective

Verify processed files are uploaded.

Command

```bash
aws s3 ls s3://datashield-s3-process-bucket
```

Expected

New processed file visible.


---

# 6. Amazon RDS

Objective

Verify metadata insertion.

Command

```bash
curl http://localhost:8000/files
```

Expected

Metadata record returned.


---

# 7. API Gateway

Objective

Verify public endpoint.

Command

```bash
curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/private/collect \
-H "Content-Type: application/json" \
-d '{"filename":"sample.json","size":123}'
```

Expected

Complete pipeline executed.


---

# 8. Application Load Balancer

Objective

Verify request routing.

Expected

Requests routed successfully.


---

# 9. Auto Scaling

Objective

Verify automatic instance launch.

Expected

New EC2 instance launched and became healthy.

---

# 10. CloudWatch

Objective

Verify monitoring.

Expected

Metrics collected.


---

# 11. SNS

Objective

Verify email notification.

Expected

Alert email received.

---

# 12. End-to-End Validation

Flow

Client

↓

API Gateway

↓

ALB

↓

Collector

↓

Archive

↓

Analyzer

↓

S3

↓

Service

↓

RDS

Expected Result

Every component worked successfully and the complete pipeline executed without errors.
