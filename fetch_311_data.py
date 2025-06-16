from sodapy import Socrata
import pandas as pd

# Initialize Socrata client (no app token, or you can add one for higher limits)
client = Socrata("data.cityofnewyork.us", None)

# Define the fields to select
fields_to_select = [
    "unique_key",
    "created_date",
    "closed_date",
    "complaint_type",
    "borough",
    "latitude",
    "longitude"
]
select_clause = ", ".join(fields_to_select)

#  Set date range for only 2024
date_filter = "created_date between '2024-01-01T00:00:00' and '2024-12-31T23:59:59'"

# Compose the full SoQL query
soql_query = f"SELECT {select_clause} WHERE {date_filter} ORDER BY :rand() LIMIT 100000"

# Fetch the data
print("Fetching random sample of 100,000 records...")
results = client.get("erm2-nwe9", query=soql_query)

# Convert to DataFrame
df = pd.DataFrame.from_records(results)

# Save to CSV
csv_filename = "311_random_sample_2024.csv"
df.to_csv(csv_filename, index=False)
print(f"Data saved to {csv_filename}")
