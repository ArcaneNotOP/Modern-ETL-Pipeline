# 🛠️ Modern ETL Pipeline

A beginner-friendly, containerized ETL pipeline built using Python, Docker, and PostgreSQL. This project demonstrates the core principles of Extract, Transform, Load (ETL) in a clean, modular format.

---

## 📦 Features

- 🔄 **Extract**: Ingests data from raw CSV files
- 🧹 **Transform**: Cleans and formats data using pandas
- 💾 **Load**: Pushes transformed data into a PostgreSQL database
- 🐳 **Dockerized**: Everything runs in isolated containers via Docker Compose
- 🧪 **Beginner-friendly**: Simple enough to learn core data engineering principles

---

## 🧰 Tech Stack

- Python 3.11
- pandas
- psycopg2 (PostgreSQL driver)
- Docker & Docker Compose
- PostgreSQL 15
- Git

---

## 🗂️ Folder Structure

```bash
modern-etl-pipeline/
├── data/              # Raw input CSV files
├── etl/               # Python scripts for ETL steps
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── requirements.txt   # Python dependencies
├── docker-compose.yml
├── .env               # Optional: environment variables
├── README.md
