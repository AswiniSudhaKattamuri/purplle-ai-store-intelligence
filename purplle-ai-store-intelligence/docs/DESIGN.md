# Purplle AI Store Intelligence - Design Document

## 1. Overview

Purplle AI Store Intelligence is an AI-powered retail analytics platform that transforms CCTV footage into actionable business intelligence.

The system uses YOLOv8 for person detection, converts detections into structured store events, stores them in SQLite, and provides real-time analytics through FastAPI APIs and a Streamlit dashboard.

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

├── Anomaly API

└── Health API

↓

Streamlit Dashboard

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

Each detected person is converted into a simulated customer journey consisting of:

* ENTRY
* ZONE_VISIT
* BILLING_QUEUE
* PURCHASE
* EXIT
* REENTRY (optional)

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
  "event_id": "uuid",
  "store_id": "STORE_001",
  "visitor_id": "VISITOR_001",
  "event_type": "ENTRY"
}
```

UUIDs are used for event identifiers to ensure uniqueness.

---

## 5. Storage Layer

SQLite is used as the event store.

Benefits:

* Lightweight
* Easy setup
* No external infrastructure
* Suitable for hackathon environments

Idempotent ingestion is implemented using:

* PRIMARY KEY(event_id)
* INSERT OR IGNORE

This prevents duplicate events from being stored.

---

## 6. Staff Handling

The platform supports staff identification using the is_staff field.

Staff events are stored but excluded from:

* Visitor metrics
* Conversion calculations
* Funnel analytics

This prevents employees from affecting customer analytics.

---

## 7. Analytics APIs

### POST /events/ingest

Stores incoming events.

### GET /stores/{store_id}/metrics

Returns:

* Unique visitors
* Staff count
* Purchase count
* Conversion rate

### GET /stores/{store_id}/funnel

Returns:

* Entry count
* Zone visits
* Billing queue visits
* Purchases
* Funnel conversion rate

### GET /stores/{store_id}/heatmap

Returns zone-level traffic distribution.

### GET /stores/{store_id}/anomalies

Detects:

* NO_ACTIVITY
* LOW_CONVERSION
* QUEUE_SPIKE
* DEAD_ZONE

### GET /health

Returns:

* System status
* Database connectivity
* Total stored events

---

## 8. Event Flow

Person Detected

↓

ENTRY Event

↓

ZONE_VISIT

↓

BILLING_QUEUE

↓

PURCHASE

↓

EXIT

↓

Optional REENTRY

↓

SQLite Storage

↓

Analytics APIs

↓

Dashboard

---

## 9. Assumptions

* YOLOv8 confidence threshold is configurable.
* SQLite is sufficient for local deployment.
* Staff identification is simulated.
* Customer journeys are simulated from detections.
* Real CCTV streams can replace image inputs with minimal architectural changes.

---

## 10. Future Improvements

* Multi-object tracking
* Real-time video stream processing
* Cross-camera visitor tracking
* Kafka-based event streaming
* PostgreSQL backend
* Live CCTV ingestion
* Advanced anomaly detection using machine learning
