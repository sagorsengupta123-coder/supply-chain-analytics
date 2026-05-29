import pandas as pd
import numpy as np

def clean_supply_delivery_data(file_path):
    print("--- Starting Data Cleaning Process ---")
    
    # Load dataset
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Successfully loaded {file_path}")
    except FileNotFoundError:
        print(f"[ERROR] File not found at {file_path}. Please check the path.")
        return None

    # 1. Handle Missing Values
    # Dynamically find which columns actually exist in the CSV file
    available_subset = [col for col in ['ID', 'Project Code', 'ProjectCode', 'Project_Code', 'Country'] if col in df.columns]
    
    # Drop rows only using the columns that exist
    df = df.dropna(subset=available_subset)

    # Fill missing values for numerical columns with median
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing values for categorical columns with 'Unknown'
    cat_cols = df.select_dtypes(exclude=[np.number]).columns
    for col in cat_cols:
        df[col] = df[col].fillna('Unknown')

    # 2. Remove Duplicates
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        df = df.drop_duplicates()
        print(f"[INFO] Removed {duplicate_count} duplicate rows.")

    # 3. Standardize Text Formatting
    df['Country'] = df['Country'].str.strip().str.title()
    df['Vendor'] = df['Vendor'].str.strip().str.upper()

    print(f"[SUCCESS] Data cleaning complete. Remaining records: {len(df)}")
    return df