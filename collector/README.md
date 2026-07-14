# Collector Service

## Overview

The Collector Service is the entry point of the DataShield platform. It receives incoming API requests, validates the request payload, creates a raw backup, and forwards the data to the Analyzer Service for processing.

## Responsibilities

- Receive client requests
- Validate incoming JSON payloads
- Create raw backup files
- Store raw backups on the Archive Server (NFS)
- Forward requests to the Analyzer Service
- Return the processing status to the client

## Technology Stack

- Python
- FastAPI
- Uvicorn
- Requests

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Service status |
| GET | /health | Health check |
| POST | /collect | Receive incoming data |

## Deployment

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8080
```

## Systemd Service

```bash
sudo systemctl start collector
sudo systemctl status collector
```

## Workflow

Client

↓

Collector

↓

Archive (Raw Backup)

↓

Analyzer

## Dependencies

See `requirements.txt`.