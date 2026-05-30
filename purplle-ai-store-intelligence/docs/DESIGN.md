# Purplle AI Store Intelligence - Design Document

## 1. Overview

This project implements an AI-powered Store Intelligence System that converts CCTV footage into business intelligence metrics.

The system detects people using YOLOv8, generates structured store events, stores them in SQLite, and exposes analytics through FastAPI endpoints.

---

## 2. System Architecture

CCTV Image / Video

↓

YOLOv8 Person Detection

↓

Event Generation Layer

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

---

## 3. Detection Pipeline

The detection pipeline uses YOLOv8 for person detection.

Input:

* CCTV frame
* Image

Output:

* Person detections
* Confidence score

Example:

```json
{
  "class": "person",
  "confidence": 0.91
}
```

Detected people are converted into ENTRY events.

---

## 4. Event Schema

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

---

## 5. Storage Layer

SQLite is used as the event store.

Benefits:

* Lightweight
* Easy setup
* No external infrastructure
* Suitable for hackathon environments

Events are stored in the events table.

---

## 6. Analytics APIs

### POST /events/ingest

Stores incoming events.

### GET /stores/{store_id}/metrics

Returns visitor metrics.

### GET /stores/{store_id}/funnel

Returns funnel statistics.

### GET /stores/{store_id}/heatmap

Returns zone-level visit counts.

### GET /stores/{store_id}/anomalies

Returns detected anomalies.

---

## 7. Event Flow

Person Detected

↓

ENTRY Event Generated

↓

Ingestion API

↓

SQLite

↓

Analytics APIs

---

## 8. Assumptions

* YOLOv8 confidence threshold is configurable.
* SQLite is sufficient for local deployment.
* Event generation is simulated using detected persons.
* Real CCTV streams can replace image inputs without major architectural changes.

---

## 9. Future Improvements

* Multi-object tracking
* Real-time video stream processing
* Stream processing with Kafka
* PostgreSQL backend
* Live dashboard
* Advanced anomaly detection
