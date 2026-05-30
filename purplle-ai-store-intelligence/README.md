# Purplle AI Store Intelligence

AI-powered Store Intelligence System built for Purplle Tech Challenge 2026.

## Overview

This project converts CCTV footage into actionable store analytics.

The system detects visitors using YOLOv8, generates structured events, stores them in SQLite, and exposes business intelligence APIs using FastAPI.

---

## Features

### Detection Pipeline

* YOLOv8 Person Detection
* Event Generation
* Confidence Scoring

### Event Ingestion

* FastAPI-based ingestion service
* Structured event schema
* SQLite event storage

### Analytics APIs

* Visitor Metrics
* Funnel Analytics
* Heatmap Analytics
* Anomaly Detection

---

## Architecture

CCTV Image / Video

↓

YOLOv8 Detection

↓

Event Generation

↓

FastAPI Ingestion

↓

SQLite

↓

Analytics APIs

├── Metrics

├── Funnel

├── Heatmap

└── Anomalies

---

## Project Structure

```text
app/
pipeline/
data/
docs/
tests/
```

---

## API Endpoints

### Health

```http
GET /health
```

### Event Ingestion

```http
POST /events/ingest
```

### Metrics

```http
GET /stores/{store_id}/metrics
```

### Funnel

```http
GET /stores/{store_id}/funnel
```

### Heatmap

```http
GET /stores/{store_id}/heatmap
```

### Anomalies

```http
GET /stores/{store_id}/anomalies
```

---

## Technology Stack

* Python
* FastAPI
* SQLite
* YOLOv8
* OpenCV
* Pydantic

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start API:

```bash
uvicorn app.main:app --reload
```

Run detection pipeline:

```bash
python pipeline/run.py
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Future Improvements

* Multi-object tracking
* Real-time CCTV streaming
* PostgreSQL
* Kafka integration
* Streamlit dashboard
* Advanced anomaly detection

---

## Author

Aswini Sudha Kattamuri
