# ✈️ Airline Reservation & Delay Analytics

## 📌 Project Overview

This project focuses on building an end-to-end data analytics pipeline for analyzing airline reservation and flight delay data. It includes data extraction, transformation, storage, processing, and visualization to generate meaningful insights.

---

## 🚀 Features

* Designed a **Data Warehouse (Star Schema)** for structured storage
* Built **ETL Pipeline using Python**
* Implemented **Advanced SQL Queries (CTE, Window Functions, Indexing)**
* Performed data processing using **Apache Spark (Batch Processing)**
* Created an **interactive dashboard using Power BI**
* Applied **data optimization techniques**
* Implemented **basic data security concepts (RBAC, masking)**

---

## 🛠️ Tech Stack

* **Programming:** Python
* **Database:** MySQL
* **Data Processing:** Apache Spark (PySpark)
* **Visualization:** Power BI
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
airline-delay-analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── sql/
│   ├── schema.sql
│   ├── queries.sql
│
├── spark/
│   ├── batch_processing.py
│   ├── streaming.py
│
├── dashboard/
│   ├── dashboard.pbix
│
├── docs/
│   ├── dashboard.png
│   ├── architecture.png
│
├── requirements.txt
└── README.md
```

---

## 🔄 ETL Pipeline

1. **Extract:** Load raw CSV dataset using Pandas
2. **Transform:** Clean data, handle null values, rename columns
3. **Load:** Insert processed data into MySQL database

---

## 🧱 Data Warehouse Design

* **Fact Table:** flight_fact
* **Dimension Tables:** airline, airport, date

---

## ⚡ SQL Features Used

* Common Table Expressions (CTE)
* Window Functions (RANK, PARTITION BY)
* Indexing for performance optimization
* Aggregation queries

---

## ⚙️ Apache Spark Processing

* Batch processing using PySpark
* Aggregation and delay analysis
* Scalable data handling

---

## 📊 Dashboard Insights

The Power BI dashboard provides:

* Average delay per airline
* Monthly delay trends
* Top delayed routes
* Key performance indicators (KPIs)

---

## 🔐 Security Implementation

* Role-Based Access Control (RBAC)
* Data masking using views

---

## 📈 How to Run the Project

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Setup Database

* Create MySQL database: `airline_db`
* Run SQL scripts from `sql/schema.sql`

### 3. Run ETL Pipeline

```
python etl/load.py
```

### 4. Run Spark Processing

```
python spark/batch_processing.py
```

### 5. Open Dashboard

* Open `dashboard/dashboard.pbix` in Power BI

---

## 📌 Key Highlights

* End-to-end data engineering workflow
* Real-world dataset analysis
* Industry-relevant tools and technologies
* Scalable and optimized solution

---

## 📎 Note

Snowflake features are conceptually implemented using MySQL for local development.

---

## 👨‍💻 Author

**Kalpesh Nayak**
B.Tech CSE | Data Engineering Enthusiast

---
