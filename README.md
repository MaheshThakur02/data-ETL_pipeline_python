# 🚀 Data ETL Pipeline with Python & PostgreSQL

This project demonstrates a simple **ETL (Extract, Transform, Load)** pipeline using **Python, pandas, and PostgreSQL**. Data is cleaned using pandas and then loaded into a PostgreSQL database using SQLAlchemy.

---

## 📌 **Project Features**

* ✅ Read and clean messy data (CSV file)
* ✅ Handle missing values with pandas
* ✅ Connect Python to **PostgreSQL** database
* ✅ Automatically create table and load data
* ✅ SQL queries to validate data insertion

---

## 📁 **Project Structure**

```
📦 data-ETL-pipeline
 ┣ 📄 car_done.csv            # Input Data File
 ┣ 📄 etl_pipeline.py         # Main ETL Python Script
 ┣ 📄 README.md               # Project Documentation
```

---

## 🛠️ **Tech Stack**

| Tool       | Description                        |
| ---------- | ---------------------------------- |
| Python     | Data extraction and transformation |
| pandas     | Data cleaning and preprocessing    |
| SQLAlchemy | Database connection (ORM)          |
| PostgreSQL | Relational database                |
| GitHub     | Version control                    |

---

## ✅ **How to Run This Project**

### 1. **Clone Repository**

```bash
git clone https://github.com/MaheshThakur02/data-ETL_pipeline_python.git
cd data-ETL_pipeline_python
```

### 2. **Install Required Libraries**

```bash
pip install pandas sqlalchemy psycopg2-binary
```

### 3. **Setup PostgreSQL Database**

* Install PostgreSQL and create a database:

```sql
CREATE DATABASE testdb;
```

### 4. **Update Database Credentials in Python Code**

In `etl_pipeline.py`:

```python
engine = create_engine('postgresql://postgres:YOUR_PASSWORD@localhost:5432/testdb')
```

### 5. **Run Python ETL Pipeline**

```bash
python etl_pipeline.py
```

---

## ✅ **Basic SQL Commands to Test**

```sql
\c testdb;
\dt;                        -- List all tables
SELECT * FROM clean_data LIMIT 5;
SELECT COUNT(*) FROM clean_data;
```

---

## 📊 **Sample Output**

```
✅ Data loaded successfully!
Table: clean_data
Total Rows After Cleaning: 117
```

---

## 📝 **Project Goals**

* Understand basic ETL pipeline structure.
* Practice SQL and pandas data cleaning.
* Learn how to integrate Python with a relational database.

---

## ✨ **Future Work**

* Add Docker Compose setup for PostgreSQL + Python
* Build API endpoint to access cleaned data
* Integrate LLM (ChatGPT) to generate SQL queries automatically

---

## 🤝 **Connect with Me**

* GitHub: [MaheshThakur02](https://github.com/MaheshThakur02)
* LinkedIn: 
* Happy to connect and collaborate!
