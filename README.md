# 🚕 GoodCabs Regional Analytics Platform  

**Databricks | Lakeflow Declarative Pipelines | Medallion Architecture**

---

## 📌 Project Overview  

GoodCabs is a fast-growing cab service company operating across multiple cities (regions). As the company scaled, regional managers started facing delayed, generic, and hard-to-use analytics, forcing teams to manually export and rework data.  

This project addresses those challenges by redesigning the data platform using **Databricks Lakeflow Spark Declarative Pipelines**, enabling faster, region-specific insights with minimal manual orchestration.  

---

## 🎯 Business Problem  

- Regional managers were not receiving data on time  
- Dashboards were generic, not region-specific  
- Heavy manual effort to transform and analyze data  

**Existing Spark pipelines were:**  
- Procedural  
- Tightly coupled  
- Hard to scale and adapt  

👉 Leadership questioned the innovation capability of the data team  

---

## ✅ Solution Approach  

We implemented a **modern declarative data pipeline** using Databricks that focuses on **_what to compute_ instead of _how to compute_**.  

### 🎯 Key Objectives  

- Deliver fast, city-level analytics  
- Reduce manual pipeline orchestration  
- Improve scalability and adaptability  
- Restore stakeholder trust through visible innovation  

---

## 🏗️ Technical Architecture  

### 🔹 Data Source  

- CSV files (simulating production ingestion)  
- Uploaded to **Amazon S3**  

**Datasets:**  
- `city.csv` → Dimension Table  
- `trips.csv` → Fact Table  

📌 *In real-world scenarios:*  
Mobile Apps → OLTP Databases → S3  

---

## 🏛️ Medallion Architecture  
