import pandas as pd
# 1. Import Member 2's functional script
from Data_Cleaning import clean_supply_delivery_data

# 2. Define the relative file path 
FILE_PATH = "supply_delivery_history.csv"

# 3. Load the cleaned dataset from the pipeline
df = clean_supply_delivery_data(FILE_PATH)

print("\n--- Starting Data Transformation Tasks ---")

# ==========================================================
# TASK A: Convert Date Columns and Calculate Delivery Lead Time
# ==========================================================
# Changing text columns back into actual dates to calculate the delivery speed
df['Scheduled Delivery Date'] = pd.to_datetime(df['Scheduled Delivery Date'])
df['Delivered to Client Date'] = pd.to_datetime(df['Delivered to Client Date'])

# Calculate the difference in days (Actual Delivery Date minus Scheduled Date)
df['Delivery_Lead_Time_Days'] = (df['Delivered to Client Date'] - df['Scheduled Delivery Date']).dt.days


# ==========================================================
# TASK B: Tag Late Deliveries (Feature Engineering)
# ==========================================================
# If days > 0, it means the delivery was late (1). Otherwise, it was on time/early (0).
df['Is_Delayed'] = df['Delivery_Lead_Time_Days'].apply(lambda x: 1 if x > 0 else 0)


# ==========================================================
# TASK C: Clean Numeric Text so we can compute Math Operations
# ==========================================================
# Removing dollar signs and commas from value columns so Python sees them as true numbers
for col in ['Line Item Value', 'Line Item Quantity']:
    df[col] = df[col].astype(str).str.replace('$', '', regex=False)
    df[col] = df[col].astype(str).str.replace(',', '', regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)


# ==========================================================
# TASK D: Create Aggregated Summary Metrics by Country
# ==========================================================
# Grouping the entire dataset by Country to find core business insights
country_summary = df.groupby('Country').agg({
    'Line Item Value': 'sum',          # Total money spent per country
    'Line Item Quantity': 'sum',       # Total packages shipped
    'Is_Delayed': 'sum'                # Count of how many shipments arrived late
}).reset_index()

# Rename columns so they look fully professional for your report
country_summary.columns = ['Country', 'Total_Shipment_Value_USD', 'Total_Quantity_Shipped', 'Total_Delayed_Shipments']


# ==========================================================
# TASK E: Display the Transformed Results
# ==========================================================
print("\n[SUCCESS] Transformation calculations completed successfully!")
print("\n--- Country Supply Chain Summary Preview ---")
print(country_summary.head())