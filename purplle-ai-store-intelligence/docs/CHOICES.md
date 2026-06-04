# Engineering Choices

## 1. Why FastAPI?

FastAPI was selected because:

* High performance
* Built-in OpenAPI documentation
* Automatic request validation using Pydantic
* Easy API development

The Swagger UI helped rapidly test and validate endpoints during development.

---

## 2. Why SQLite?

SQLite was selected because:

* Lightweight
* Zero configuration
* No external server required
* Easy portability

For a hackathon environment, SQLite provides a simple and reliable event store.

---

## 3. Why YOLOv8?

YOLOv8 was selected because:

* Fast inference speed
* Good detection accuracy
* Strong community support
* Easy integration with Python and OpenCV

The model is capable of detecting people in CCTV-style imagery with confidence scores.

---

## 4. Why Event-Driven Architecture?

The system follows an event-driven design.

Detection and analytics are separated using events.

Benefits:

* Loose coupling
* Easier scaling
* Better maintainability
* Future support for streaming platforms such as Kafka

---

## 5. Why REST APIs?

REST APIs provide:

* Simplicity
* Interoperability
* Easy integration with dashboards
* Clear separation between ingestion and analytics

---

## 6. Trade-Offs

### SQLite

Pros:

* Easy setup
* Lightweight

Cons:

* Not suitable for very high throughput systems

---

### YOLOv8

Pros:

* Fast
* Accurate

Cons:

* Detection quality depends on image quality
* May require fine-tuning for specific retail environments

---

### Event Simulation

Pros:

* Easy to demonstrate architecture
* Enables rapid development

Cons:

* Does not represent full production CCTV complexity

---

## 7. Additional Engineering Decisions

### Why UUID Event IDs?

UUIDs are used as event identifiers to guarantee uniqueness across all generated events.

Benefits:

* Prevents ID collisions
* Supports distributed event generation
* Improves event traceability

---

### Why Idempotent Ingestion?

The ingestion API uses:

* PRIMARY KEY(event_id)
* INSERT OR IGNORE

Benefits:

* Prevents duplicate event storage
* Safe retry behavior
* Improves production reliability

---

### Why Staff Filtering?

Retail analytics should focus on customer behavior rather than employee movement.

Staff events are stored but excluded from:

* Visitor metrics
* Funnel calculations
* Conversion rate calculations

This provides more accurate business insights.

---

### Why Unique Visitor-Based Conversion Rate?

Retail conversion rate should measure how many unique visitors completed a purchase rather than counting total purchase events.

The system calculates conversion rate using:

* Unique purchasing visitors
* Unique store visitors

Benefits:

* Prevents conversion rates from exceeding 100%
* Avoids double-counting repeat purchase events
* Produces more accurate business intelligence metrics
* Aligns with standard retail analytics practices

This approach ensures that conversion analytics reflect actual customer behavior rather than raw event counts.


### Why Streamlit?

Streamlit was selected because:

* Rapid dashboard development
* Easy integration with FastAPI
* Built-in charts and tables
* Suitable for analytics visualization

It enabled fast creation of a retail intelligence dashboard without requiring frontend frameworks.

---

## 8. Production Improvements

If deployed in production:

* PostgreSQL would replace SQLite
* Kafka would be used for event streaming
* Multi-object tracking would be added
* Cross-camera visitor tracking would be implemented
* Real-time CCTV streams would replace static images
* Advanced anomaly detection models would be introduced
* Cloud deployment and monitoring would be added

---

## 9. Key Enhancements Implemented

The final solution includes several enhancements beyond the basic architecture:

* UUID-based event generation
* Idempotent event ingestion
* Staff-aware analytics
* Conversion rate calculation
* Funnel analytics
* Heatmap analytics
* Health monitoring endpoint
* Anomaly detection:

  * NO_ACTIVITY
  * LOW_CONVERSION
  * QUEUE_SPIKE
  * DEAD_ZONE
* Streamlit analytics dashboard
* Automated test suite

---

## 10. Conclusion

The chosen architecture prioritizes simplicity, scalability, maintainability, and ease of demonstration while preserving a clear upgrade path toward a production-scale AI-powered store intelligence platform.

The design separates detection, event processing, storage, analytics, and visualization layers, making the system easy to extend and evolve as requirements grow.
