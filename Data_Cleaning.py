import pandas as pd
import re


def handle_missing_values(df):
    """
    Handles missing values in the dataset.
    Numeric columns are filled with median values.
    Text columns are filled with 'Unknown'.
    """
    df = df.copy()

    for column in df.columns:
        if df[column].dtype in ["int64", "float64"]:
            df[column] = df[column].fillna(df[column].median())
        else:
            df[column] = df[column].fillna("Unknown")

    return df


def standardize_date_columns(df):
    """
    Converts date-like columns into standard YYYY-MM-DD format.
    """
    df = df.copy()

    for column in df.columns:
        if "date" in column.lower():
            df[column] = pd.to_datetime(df[column], errors="coerce").dt.strftime("%Y-%m-%d")

    return df


def clean_numeric_text_column(df, column_name):
    """
    Removes non-numeric characters from cost and weight columns.
    Example: '$1,200 kg' becomes 1200.
    """
    df = df.copy()

    if column_name in df.columns:
        df[column_name] = (
            df[column_name]
            .astype(str)
            .str.replace(r"[^0-9.]", "", regex=True)
        )
        df[column_name] = pd.to_numeric(df[column_name], errors="coerce")

    return df


def clean_supply_delivery_data(file_path):
    """
    Main function to clean supply delivery dataset.
    """
    try:
        df = pd.read_csv(file_path)

        df = handle_missing_values(df)
        df = standardize_date_columns(df)

        possible_cost_columns = ["cost", "delivery_cost", "shipping_cost"]
        possible_weight_columns = ["weight", "package_weight", "shipment_weight"]

        for col in possible_cost_columns:
            df = clean_numeric_text_column(df, col)

        for col in possible_weight_columns:
            df = clean_numeric_text_column(df, col)

        print("Data cleaning completed successfully.")
        print(df.head())

        return df

    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


if __name__ == "__main__":
    clean_supply_delivery_data("supply_delivery_history.csv")