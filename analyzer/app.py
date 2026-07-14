from fastapi import FastAPI
from datetime import datetime
import requests
import boto3
import json

app = FastAPI()

s3 = boto3.client("s3")

BUCKET = "Bucket-Name"


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze(payload: dict):

    filename = f"processed_{int(datetime.now().timestamp())}.json"

    # Upload to S3
    s3.put_object(
        Bucket=BUCKET,
        Key=filename,
        Body=json.dumps(payload)
    )

    metadata = {
        "file": filename,
        "size": len(json.dumps(payload))
    }

    metadata_result = "not_sent"

    try:
        response = requests.post(
            "archive-collector-metadata-endpoint",
            json=metadata,
            timeout=5
        )

        metadata_result = {
            "status_code": response.status_code,
            "response": response.text
        }

        print("Metadata sent successfully")
        print(metadata_result)

    except Exception as e:
        print("Metadata notification failed:", str(e))

        metadata_result = {
            "error": str(e)
        }

    return {
        "status": "uploaded",
        "file": filename,
        "metadata": metadata_result
    }