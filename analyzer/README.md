# Analyzer Service

## Overview

The Analyzer Service processes data received from the Collector Service. It generates processed output files, uploads them to Amazon S3, and sends metadata to the Service Layer.

## Responsibilities

- Receive requests from Collector
- Process incoming data
- Generate processed JSON files
- Upload processed files to Amazon S3
- Send metadata to the Service Layer

## Technology Stack

- Python
- FastAPI
- Uvicorn
- Boto3
- Requests

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /health | Health check |
| POST | /analyze | Process incoming data |

## Deployment

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8081
```

## Systemd Service

```bash
sudo systemctl start analyzer
sudo systemctl status analyzer
```

## Workflow

Collector

↓

Analyzer

↓

Amazon S3

↓

Service Layer

## Dependencies

See `requirements.txt`.