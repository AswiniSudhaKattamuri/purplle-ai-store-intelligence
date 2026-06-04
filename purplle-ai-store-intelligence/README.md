# Purplle AI Store Intelligence

AI-powered Store Intelligence System built for Purplle Tech Challenge 2026.

## Overview

Purplle AI Store Intelligence converts CCTV footage into actionable retail analytics.

The system uses YOLOv8 for person detection, generates structured retail events, stores them in SQLite, and exposes business intelligence insights through FastAPI APIs and a Streamlit dashboard.

---

## Features

### Detection Pipeline

* YOLOv8 Person Detection
* Confidence Scoring
* Event Generation Pipeline

### Event Processing

* Structured Event Schema
* FastAPI Event Ingestion
* SQLite Event Storage
* Idempotent Event Handling

### Analytics APIs

* Visitor Metrics
* Funnel Analytics
* Heatmap Analytics
* Anomaly Detection

### Dashboard

* Store Metrics
* Conversion Funnel
* Zone Heatmaps
* Operational Anomalies

---

## System Architecture

CCTV Image / Video

↓

YOLOv8 Detection

↓

Event Generation

↓

FastAPI Ingestion API

↓

SQLite Event Store

↓

Analytics Layer

├── Metrics API

├── Funnel API

├── Heatmap API

└── Anomaly API

↓

Streamlit Dashboard

---

## Project Structure

```text
app/
├── anomalies.py
├── database.py
├── funnel.py
├── health.py
├── heatmap.py
├── ingestion.py
├── main.py
├── metrics.py
└── models.py

pipeline/
├── detect.py
├── emit.py
├── run.py
└── tracker.py

dashboard/
└── app.py

tests/

docs/
├── DESIGN.md
└── CHOICES.md

data/
```

## Event Schema

Each event contains:

* event_id
* store_id
* camera_id
* visitor_id
* event_type
* timestamp
* zone_id
* dwell_ms
* is_staff
* confidence

Example:

```json
{
  "event_id": "1",
  "store_id": "STORE_001",
  "visitor_id": "VISITOR_001",
  "event_type": "ENTRY"
}
```

## API Endpoints

### Health Check

```http
GET /health
```

### Event Ingestion

```http
POST /events/ingest
```

### Visitor Metrics

```http
GET /stores/{store_id}/metrics
```

### Funnel Analytics

```http
GET /stores/{store_id}/funnel
```

### Heatmap Analytics

```http
GET /stores/{store_id}/heatmap
```

### Anomaly Detection

```http
GET /stores/{store_id}/anomalies
```

---

## Dashboard Capabilities

The Streamlit dashboard provides:

* Visitor Count
* Staff Count
* Purchase Count
* Conversion Rate
* Funnel Visualization
* Heatmap Visualization
* Anomaly Alerts

---

## Technology Stack

* Python
* FastAPI
* SQLite
* Streamlit
* YOLOv8
* OpenCV
* Pydantic
* Pytest

---

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

### Run Detection Pipeline

```bash
python pipeline/run.py
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

### Run Tests

```bash
pytest
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Screenshots

### Dashboard Overview

* Visitor Metrics
* Conversion Analytics
* Funnel Visualization

### Dashboard Analytics

* Heatmap Analytics
* Anomaly Detection

### Swagger Documentation

* API Testing Interface

### YOLO Detection Validation

* Person Detection Output

---

## Testing

The project includes automated tests for:

* Health Endpoint
* Metrics API
* Funnel Analytics
* Anomaly Detection
* Detection Pipeline

```text
5 Tests Passed
```

---
## Validation Results

The detection pipeline was validated using multiple retail-style images and videos with varying visitor densities.

Sample validation outcomes:

* Video 1: 4 unique visitors detected with a 25% conversion rate.
* Video 2: 7 unique visitors detected with a 28.57% conversion rate.
* Additional test videos were processed to verify analytics consistency across different customer densities and store layouts.

The system successfully generated structured retail events, populated the analytics database, and produced dashboard visualizations for metrics, funnel analytics, heatmaps, and anomaly detection.

Known limitations include mirror reflections and severe occlusions, which may occasionally result in additional detections. These can be further improved through multi-object tracking and retail-specific model fine-tuning.


## Future Improvements

* Multi-Object Tracking (DeepSORT / ByteTrack)
* Real-Time CCTV Stream Processing
* Kafka Event Streaming
* PostgreSQL Backend
* Advanced AI-Based Anomaly Detection
* Authentication and Access Control
* Cloud Deployment

---

## Author

Aswini Sudha Kattamuri

Purplle Tech Challenge 2026 Submission
