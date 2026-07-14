from fastapi import FastAPI
from datetime import datetime
import requests
import json

app = FastAPI()

ANALYZER_URL = "ANALYZER-URL"

@app.get("/")
def root():
    return {"message":"collector running"}

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.post("/private/collect")
def collect_api_gateway(payload: dict):
    return collect(payload)

@app.post("/collect")
def collect(payload: dict):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Collector Log
    with open("/tmp/collector.log","a") as f:
        f.write(f"{datetime.now()} {payload}\n")

    # Raw Backup to Archive
    backup_file = f"/archive-backups/raw_{timestamp}.json"

    with open(backup_file,"w") as f:
        json.dump(payload,f,indent=4)

    # Forward to Analyzer
    response = requests.post(
        ANALYZER_URL,
        json=payload
    )

    return {
        "status":"forwarded",
        "backup_file": backup_file,
        "analyzer_response": response.json()
    }