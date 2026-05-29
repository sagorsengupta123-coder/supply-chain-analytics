# Supply Chain Analytics Pipeline
### 🔗 Project Resources
* **GitHub Repository:** [https://github.com/sagorsengupta123-coder/supply-chain-analytics]
* **Taiga Project Board:** [https://tree.taiga.io/project/sagorsengupta123-coder-supply-chain-analytics-sprint/timeline]
## 👥 Group Members & Roles
* **Sagor** – Project Manager / Scrum Master
* **Riddhi** – Data Cleaning Specialist (`Data_Cleaning.py`)
* **Bogapriya Muralikannan** – Data Transformation Engineer (`data_transformation.py`)
* **Priti** – Data Analyst & Visualizer (`analysis.py`)
* **Sulav** – Business Intelligence & Insights Analyst

---

## 📋 Project Overview
This project establishes an integrated, end-to-end Python data pipeline designed to clean, transform, and analyze international supply chain delivery logs (`supply_delivery_history.csv`). The script dynamically processes over 10,000 shipment records to track fulfillment schedules, manage exceptions, and isolate key performance metrics across global distribution routes.

---

## ⚙️ Pipeline Architecture & Workflow

The system is constructed as a modular execution chain, allowing independent development while maintaining unified execution through a single main controller:

1. **Ingestion & Data Cleaning (`Data_Cleaning.py`)**
   * Dynamically maps variable dataset columns (`Project Code` variants).
   * Validates records, purges duplicate shipment rows, and handles missing country variables.

2. **Feature Engineering & Transformation (`data_transformation.py`)**
   * Implements robust date-time casting with error-coercion algorithms to cleanly neutralize corrupted string inputs (such as `"TBD"` or erroneous date values).
   * Calculates structural lead times and formats downstream analytical metrics.

3. **Statistical Summary & Visualization (`analysis.py`)**
   * Functions as the master execution file.
   * Generates deep-dive missing value matrices, summary statistics, and automated volumetric charts profiling shipment frequencies by nation.

---

## 🚀 How to Run the Pipeline

To execute the entire pipeline from scratch, ensure you have the dataset placed in the project root directory and run the master analysis script:

```bash
python analysis.py
