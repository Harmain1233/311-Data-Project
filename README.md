# NYC 311 Complaint Types Analysis (January 2023)

This project analyzes New York City's 311 service requests from January 2023 to identify trends in complaint types, peak hours, and resolution efficiency across boroughs. The analysis combines Python-based preprocessing with an interactive Tableau dashboard to communicate insights effectively.

**Key Insight:**  
Brooklyn had the highest volume of complaints—primarily illegal parking. Reports peaked between 10:00 AM and 2:00 PM, likely due to commuter congestion.

---

## Dashboard Preview

<p align="center">
  <img width="720" alt="NYC 311 Dashboard" src="https://github.com/user-attachments/assets/183298e1-c313-497d-8ab0-2d2628d07029" />
</p>

**View the live dashboard:**  
🔗 [Tableau Public – NYC 311 Complaint Dashboard](https://public.tableau.com/app/profile/harmain.munir/viz/311ServiceRequests_17486660581880/Dashboard1)

---

## Key Visuals & Features

- **Service Request Density Map** – Geographic concentration of complaints across NYC
- **Hourly Complaint Trends** – Volume by hour across boroughs
- **Top Complaint Types** – Most frequently reported issues (e.g., Illegal Parking, Noise)
- **Resolution Time per Borough** – Average complaint resolution time by location
- **Complaint Type vs Borough Heatmap** – Matrix showing complaint distribution

---

## Tools & Technologies

- **Python** – Data extraction and preprocessing
- **pandas** – Data manipulation and transformation
- **Jupyter Notebook** – Exploratory and reproducible analysis
- **Socrata API (SODA)** – Accessed NYC Open Data programmatically
- **Tableau Public** – Interactive data visualization and dashboard design

---

## Data Preparation Workflow

All cleaning and transformation steps were executed using `pandas` in Jupyter Notebook.  
Key preprocessing actions included:

1. Filtering the dataset for January 2023
2. Parsing datetime fields and calculating resolution time (in days)
3. Dropping records with missing borough or date values
4. Removing unnecessary columns (`latitude`, `longitude`)
5. Rounding resolution time for readability
6. Saving the cleaned data for Tableau use

> See: [`311_week1_data_cleaning.ipynb`](./311_week1_data_cleaning.ipynb)

---

## Data Source

The dataset was retrieved from the NYC Open Data portal:  
🔗 [311 Service Requests (2010–Present)](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

---

## Reflections & Takeaways

Through this project, I gained practical experience in:

- Cleaning real-world datasets using Python
- Leveraging open civic data through APIs
- Structuring Tableau dashboards to emphasize key insights
- Applying analytical thinking to urban services and citizen feedback

---

## About the Author

**Harmain Munir**  
Computer Science Graduate · Data & Software Enthusiast  
[LinkedIn](https://www.linkedin.com/in/harmainmunir) · [GitHub](https://github.com/Harmain1233)

---
