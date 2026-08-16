1. SYSTEM ARCHITECTURE DIAGRAM

```text
[IoT Sensors on Turbines] 
           │
           ▼
[Message Queue: Apache Kafka] (Decouples high-velocity ingestion stream)
           │
           ▼
[Stream Processor: AWS Lambda] (Executes real-time anomaly detection)
           │
           ├───► [Time-Series DB / Hot Storage] (Past 30 days rapid querying)
           │
           └───► [Amazon S3 / Cold Storage] (Long-term historical archiving)

2. KEY FINDINGS
After running the programmatic data processing pipeline against the streaming telemetry dataset, specific wind turbines consistently violated the safe operational thresholds (Temperature > 85.0°C or Vibration > 15.0 mm/s).

The specific Turbine IDs requiring urgent onsite engineering maintenance and immediate inspection are:

T-04, T-07

Total Anomaly Events Logged: 1,017


3. ARCHITECTURAL JUSTIFICATION
The legacy single-server architecture represents a catastrophic single point of failure vulnerable to ingestion traffic spikes. Implementing a distributed message queue (such as Apache Kafka) decouples the incoming high-velocity data stream from the downstream processing layers. This infrastructure acts as a buffer, guaranteeing zero data loss during high-load intervals.

Downstream, decoupled stream processors (like AWS Lambda) auto-scale independently to execute real-time anomaly detection smoothly without causing server resource exhaustion.


4. COST-OPTIMIZATION STRATEGY
To maintain strict financial efficiency, a Tiered Storage Strategy is utilized. High-velocity data from the past 30 days will reside in a specialized Time-Series Database ("Hot Storage") for rapid analytical querying and operations.

Historical telemetry data will automatically transition via automated lifecycle policies into low-cost cloud object storage like Amazon S3 ("Cold Storage"). This drastically reduces ongoing infrastructure overhead while preserving data logs for training predictive machine learning models.