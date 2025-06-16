# NYC 311 Complaint Types Analysis (Jan 2023)

This project analyzes NYC 311 service request data from January 2023 to uncover complaint trends across boroughs, peak reporting times, and resolution efficiency. The project combines Python-based data preprocessing with an interactive Tableau dashboard.

> 🗝️ **Key Insight:** Brooklyn had the highest volume of complaints, mostly illegal parking. Activity peaked between 10 AM – 2 PM, likely due to commuter congestion.

---

## 📊 Dashboard Overview

 <img width="726" alt="Screenshot 2025-06-15 at 11 31 32 PM" src="https://github.com/user-attachments/assets/183298e1-c313-497d-8ab0-2d2628d07029" />



- 🗺️ **Density Map**: Visualizes complaint concentration across NYC
- 📈 **Hourly Trends**: Shows when complaints peaked by borough
- 🔥 **Top Complaint Types**: Highlights most frequent issues (e.g., Illegal Parking, Heat/Hot Water)
- ⚖️ **Resolution Time Chart**: Compares average resolution days across boroughs
- 🧩 **Heatmap Matrix**: Cross-tabulates complaint types by borough

👉 **[View the Tableau Dashboard](https://public.tableau.com/app/profile/harmain.munir/viz/311ServiceRequests_17486660581880/Dashboard1)**

---

## 🧪 Tools & Technologies
- **Python** – Data preprocessing and cleaning
- **Jupyter Notebook** – Documenting and transforming the dataset
- **pandas** – Handling and analyzing tabular data
- **Tableau Public** – Designing interactive visualizations
- **Socrata Open Data API (SODA)** – Downloaded raw 311 data from NYC Open Data Portal

---

## 🛠️ Data Cleaning Steps

1. Filtered the dataset to include only **January 2023** requests
2. Dropped rows with missing `created_date`, `closed_date`, or `borough`
3. Calculated **Resolution Time (days)** from request to resolution
4. Removed unnecessary columns like `latitude` and `longitude`
5. Exported a cleaned CSV file for Tableau use

> See full cleaning logic in: [`311_week1_data_cleaning.ipynb`](./311_week1_data_cleaning.ipynb)

---

## 📂 Data Source

Data is publicly available from the NYC Open Data Portal:  
🔗 [311 Service Requests from 2010 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

---

## 🧠 What I Learned

- Hands-on experience with the full data analytics lifecycle
- Efficiently wrangling large datasets using `pandas`
- Designing dashboards for **insight clarity and storytelling**
- Leveraging open data to drive meaningful civic insights

---

## ✨ Author

**Harmain Munir** – Data Enthusiast | Software Engineer  

---
