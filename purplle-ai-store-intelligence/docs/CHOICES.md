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

## 7. Production Improvements

If deployed in production:

* PostgreSQL would replace SQLite
* Kafka would be used for event streaming
* Multi-object tracking would be added
* Real-time CCTV streams would replace static images
* Advanced anomaly detection models would be introduced

---

## 8. Conclusion

The chosen architecture prioritizes simplicity, scalability, and ease of demonstration while preserving a clear upgrade path toward a production-scale store intelligence platform.
