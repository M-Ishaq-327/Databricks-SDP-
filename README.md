# Databricks-SDP-
🚕 GoodCabs Regional Analytics Platform

Databricks | Lakeflow Declarative Pipelines | Medallion Architecture

📌 Project Overview

GoodCabs is a fast-growing cab service company operating across multiple cities (regions). As the company scaled, regional managers started facing delayed, generic, and hard-to-use analytics, forcing teams to manually export and rework data.

This project addresses those challenges by redesigning the data platform using Databricks Lakeflow Spark Declarative Pipelines, enabling faster, region-specific insights with minimal manual orchestration.

🎯 Business Problem
Regional managers were not receiving data on time
Dashboards were generic, not region-specific
Heavy manual effort to transform and analyze data
Existing Spark pipelines were:
Procedural
Tightly coupled
Hard to scale and adapt
Leadership questioned the innovation capability of the data team
✅ Solution Approach

We implemented a modern declarative data pipeline using Databricks that focuses on what to compute instead of how to compute.

Key Objectives:
Deliver fast, city-level analytics
Reduce manual pipeline orchestration
Improve scalability and adaptability
Restore stakeholder trust through visible innovation
🏗️ Technical Architecture
🔹 Data Source
CSV files (simulating production ingestion)
Uploaded to Amazon S3
Represents:
city.csv → Dimension Table
trips.csv → Fact Table

In real-world scenarios, data would flow from mobile apps → OLTP databases → S3.

🔹 Architecture Pattern

Medallion Architecture

S3 → Bronze → Silver → Gold
Bronze Layer
Raw ingestion from S3
Schema enforcement
Silver Layer
Cleaned & enriched data
Fact–Dimension joins
Gold Layer
Aggregated, business-ready tables
Optimized for analytics
🔹 Pipeline Type
Lakeflow Spark Declarative Pipelines
Automatic:
Dependency management
Incremental processing
Execution optimization
📊 Analytics Use Cases (Gold Layer)

Region (City) level metrics:

Average passenger rating
Average driver rating
Total number of rides
Total revenue per city
Distance-based insights

These outputs are designed specifically for regional / city managers.

🧱 Data Model
📌 Dimension Table

City

city_id
city_name
📌 Fact Table

Trips

trip_id
city_id
fare_amount
passenger_rating
driver_rating
distance_traveled
trip_timestamp
🔐 Governance & Security
Unity Catalog used for:
Data access control
Schema governance
Table-level permissions
🧠 Tools & Technologies
Databricks
Apache Spark
Lakeflow Declarative Pipelines
Amazon S3
Unity Catalog
Delta Lake
SQL & PySpark
🚀 Key Outcomes
⚡ Faster regional insights
🔁 Reduced manual pipeline orchestration
📈 Scalable and modular data architecture
💡 Demonstrates innovation using modern Databricks features
🧩 Clear separation of raw, refined, and business data
📁 Repository Structure
├── data/
│   ├── city.csv
│   └── trips.csv
├── bronze/
├── silver/
├── gold/
├── notebooks/
├── architecture/
│   └── architecture_diagram.png
└── README.md
🧪 Project Focus

This project focuses on data engineering architecture and pipeline design.
Dashboard creation is intentionally out of scope.

🏁 Final Notes

This project showcases:

Real-world data engineering problem solving
Declarative pipeline design
Enterprise-grade analytics architecture
Stakeholder-driven solution thinking
