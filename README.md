# manufacturing-data-platform
End-to-End Manufacturing Data Engineering Pipeline using Python, Airflow, Docker, PostgreSQL and Power BI.

## Project Overview

This project demonstrates an end-to-end Data Engineering Pipeline for a manufacturing dataset. The pipeline extracts raw manufacturing data, transforms it into meaningful insights, loads it into PostgreSQL, and visualizes the results using Power BI.

The project follows a Medallion Architecture (Bronze, Silver, Gold) and uses Apache Airflow to automate the ETL workflow.

---

## 🎯 Objectives

- Build an automated ETL pipeline.
- Store processed data in PostgreSQL.
- Create Bronze, Silver, and Gold data layers.
- Generate summary tables for business analysis.
- Build an interactive Power BI dashboard.

---

## Tech Stack

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Apache Airflow
* Docker
* Power BI
* Git & GitHub

---

## Architecture

CSV Dataset

↓

Python ETL

↓

Bronze Layer

↓

Silver Layer

↓

Gold Layer

↓

PostgreSQL

↓

Power BI Dashboard

---

## ⚙️ ETL Workflow

### 1. Extract

- Load manufacturing dataset (AI4I 2020).
- Store raw data in the Bronze layer.

### 2. Transform

- Clean missing values.
- Prepare analytical columns.
- Generate business summary tables.
- Store processed data in the Silver and Gold layers.

### 3. Load

- Load processed data into PostgreSQL.
- Create summary tables:
  - Machine Health
  - Manufacturing Summary
  - Failure Type Summary
  - Product Type Summary
  - RPM Summary
  - Temperature Summary
  - Tool Wear Summary

### 4. Orchestration

Apache Airflow automates the ETL process using DAG scheduling.

### 5. Visualization

Power BI connects to PostgreSQL and displays interactive dashboards.

---

## Dashboard KPIs

* Total Machines
* Total Failures
* Failure Rate
* Average Tool Wear
* Average RPM
* Average Torque

---

## Dashboard Visualizations

* Failure by Failure Type
* Product Type Distribution
* Failure by Tool Wear Group
* RPM vs Torque Analysis
* Failure Type Matrix
* Failure Rate by Product Type

---

## 📂 Project Structure

manufacturing-data-platform/

├── dags/

│   └── manufacturing_etl_dag.py

├── scripts/

│   ├── extract.py

│   ├── transform.py

│   ├── load.py

│   └── etl_pipeline.py

├── data/

│   ├── bronze/

│   ├── silver/

│   └── gold/

├── dashboard/

│   └── manufacturing_report.pbix

├── images/

├── requirements.txt

├── docker-compose.yaml

├── airflow.cfg

└── README.md

---

## ▶️ How to Run

1. Clone the repository.

2. Install dependencies

pip install -r requirements.txt

3. Start Docker

docker-compose up

4. Start Airflow

5. Trigger the Manufacturing ETL DAG

6. Verify data in PostgreSQL.

7. Open the Power BI dashboard.

---

## Future Improvements

* Cloud deployment (AWS/Azure)
* Integrate Apache Kafka for streaming data
* Process large datasets using PySpark
* Add real-time monitoring
* Automate Power BI refresh

---

## 👨‍💻 Author

**Tushant Chaudhari**

GitHub:
https://github.com/tushantac2003-prog
