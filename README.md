# Exploring-Ola-Ride-Data-A-Data-Analysis-Approach

---
## About the dashboard
This project presents a complete data analysis pipeline for a ride-hailing service's operational data in Bengaluru. It starts with **data loading and feature engineering using Python** and culminates in an **interactive, three-page dashboard** built with Google Looker Studio. The primary objective is to move beyond simple reporting by diagnosing the core business problem—**high cancellation rates**—and providing data-driven recommendations for strategic driver deployment and customer experience improvements.

---

---
## Access the Interactive Dashboard
You can access the live, interactive dashboard using the following link:https://lookerstudio.google.com/s/iSGx0yFhhXM
---

---

##  Python Analysis Phase (Data Preparation & EDA)

Before visualization, the raw data required significant cleaning and feature engineering to derive actionable metrics. Three Python scripts were used for this phase:

### 1. `Data_Loading.py`

This script handles the initial setup.

* **Purpose:** Loads the raw `Bengaluru Ola.csv` file into a pandas DataFrame.
* **Key Functionality:** It includes a `try-except` block to ensure robust file loading, strips whitespace from column names, and prints a summary of initial missing values. This step confirms the data is accessible and identifies initial data quality issues.

### 2. `Data_Cleaning_and_Feature_Engineering.py`

This is the core data transformation script that creates the dataset used for the dashboard.

* **Data Cleaning:** It standardizes the date and time columns, handles missing values (e.g., filling `Booking Value` with 0 for canceled/incomplete rides), and fills categorical fields like `Reason for Cancelling` with "Not Cancelled."
* **Feature Engineering:** Critical metrics were calculated here, including:
    * **`Day_of_Week` and `Hour_of_Day`**: Essential for analyzing demand patterns.
    * **`Is_Cancelled`**: A binary flag (1 or 0) used to isolate cancellation events.
    * **`Cost_Per_KM`**: A financial metric used to evaluate the potential profitability of various ride types.
* **Output:** Generates the clean and feature-rich `advanced_bengaluru_ola_dataset.csv` used as the dashboard's data source.

### 3. `EDA.py`

This script was used to generate static plots to validate the data and pre-discover major insights before building the interactive dashboard.

* **Purpose:** Confirms data distributions and tests hypotheses (e.g., are cancellations tied to a specific vehicle type?).
* **Output:** Generated initial charts for **Booking Status Distribution**, **Busiest Hours of the Day**, and **Top Cancellation Reasons** by both customer and driver. The findings directly informed the layout and focus of the Looker Studio dashboard pages.

---

##  Page 1: Overview & Key Metrics

This page establishes the baseline performance and scale of the business.

### Visualizations & Insights

1.  **Scorecards (Total Rides, Total Revenue, Avg Distance)**
    * **Insight:** These KPIs quantify the market presence and financial value of the average transaction. For instance, the **Average Ride Distance** is a critical indicator of whether the business is primarily serving short-haul commuters or longer inter-city trips.
2.  **Time Series Chart (Ride Trends Over Time)**
    * **Insight:** This visualization highlights **demand volatility**, pinpointing specific days or hours when the booking volume reliably peaks (e.g., during rush hours or on weekends).
    * **Action:** This data is vital for **predictive capacity planning**—ensuring adequate driver supply during these predictable peak periods to prevent service decline.
3.  **Pie Chart (Booking Status Distribution)** 
    * **Insight:** This is the most crucial health check. It quantifies the lost revenue by showing the proportion of **Cancelled** and **Incomplete** rides versus successful ones. The total size of the non-successful slices directly represents the operational efficiency gap.

---

##  Page 2: Deep Dive into Cancellations

This page shifts focus to root-cause analysis, breaking down the friction by stakeholder.

### Visualizations & Insights

1.  **Bar Chart (Customer Cancellation Reasons)** 
    * **Insight:** The top reasons often point to **Service Delivery Failure**. For example, if **"Driver took too long to arrive"** is the primary cause, the issue is with the system's ability to fulfill the promise of a quick ride.
    * **Action:** Policy changes should target these issues, potentially including harsher penalties for drivers who reject rides or misuse the system, and a more robust ETA algorithm.
2.  **Bar Chart (Driver Cancellation Reasons)** 
    * **Insight:** The reasons here highlight **Driver Risk and Profitability Concerns**. Common issues like "The customer was coughing/sick" or "More than permitted people" are drivers managing personal safety or rejecting unprofitable/inconvenient rides.
    * **Action:** Requires **targeted incentives** or policy clarity on ride capacity to address driver concerns without compromising service reliability.
3.  **Table (Cancellation Rate by Vehicle Type)**
    * **Insight:** This is the **Problem Segment Identifier**. It uses the corrected `Cancellation Rate` metric to show which vehicle type (e.g., Mini, Auto, Prime Sedan) has the highest failure rate.
    * **Action:** Intervention should be **data-driven and segment-specific**. The company must investigate the incentives and policy constraints for the vehicle type with the highest cancellation rate to bring its performance in line with the others.

---

##  Page 3: Optimization:Location & Customer Experience

This page provides the actionable steps for improving service quality and operational metrics.

### Visualizations & Insights

1.  **Bar Chart (Top High-Demand Pickup Locations)** 
    * **Insight:** Identifies the **Geographic Hotspots** that drive the majority of bookings and revenue.
    * **Action:** These areas must receive the highest priority for **driver deployment**. By strategically clustering drivers here, the company can directly lower customer wait times (CTAT).
2.  **Time Series Chart (Customer & Driver Rating Trends)**
    * **Insight:** Acts as the **Service Quality Report Card**. Shows whether satisfaction is rising, stable, or falling. A divergence (e.g., Driver Rating rising, Customer Rating falling) points to a policy imbalance.
    * **Action:** Any sharp drop in either trend should trigger an immediate **Root Cause Analysis** on the day of the drop to isolate the cause (e.g., system error, pricing change, or external event).
3.  **Scorecards (Avg VTAT & Avg CTAT)**
    * **Insight:** These are the **Execution Benchmarks**. **Avg CTAT (Customer Acceptance Time)** is the most critical metric for customer experience, directly linked to customer cancellations.
    * **Action:** The operations team should be tasked with setting and achieving a target reduction for the Avg CTAT. Reducing this metric is the most effective way to improve the customer experience and recover lost revenue identified on Page 2.
