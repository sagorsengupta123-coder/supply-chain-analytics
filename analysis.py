import pandas as pd
import matplotlib.pyplot as plt

from Data_Cleaning import clean_supply_delivery_data


def basic_info(df):
    """Display basic information about the dataset."""
    print("\n--- BASIC DATASET INFORMATION ---")
    print("Rows and Columns:", df.shape)
    print("Column Names:", df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)


def missing_values_summary(df):
    """Return missing values count for each column."""
    print("\n--- MISSING VALUES SUMMARY ---")
    return df.isnull().sum()


def summary_statistics(df):
    """Return summary statistics for numeric columns."""
    print("\n--- SUMMARY STATISTICS ---")
    return df.describe()


def top_countries_by_records(df, n=10):
    """Return top countries by number of shipment records."""
    print(f"\n--- TOP {n} COUNTRIES BY SHIPMENT RECORDS ---")
    result = df["Country"].value_counts().head(n)
    print(result)
    return result


def top_vendors_by_records(df, n=10):
    """Return top vendors by number of shipment records."""
    print(f"\n--- TOP {n} VENDORS BY SHIPMENT RECORDS ---")
    result = df["Vendor"].value_counts().head(n)
    print(result)
    return result


def shipment_mode_summary(df):
    """Return shipment mode distribution."""
    print("\n--- SHIPMENT MODE SUMMARY ---")
    result = df["Shipment Mode"].value_counts()
    print(result)
    return result


def product_group_summary(df):
    """Return product group distribution."""
    print("\n--- PRODUCT GROUP SUMMARY ---")
    result = df["Product Group"].value_counts()
    print(result)
    return result


def country_product_group_summary(df):
    """Return shipment count by country and product group."""
    print("\n--- COUNTRY AND PRODUCT GROUP SUMMARY ---")
    result = (
        df.groupby(["Country", "Product Group"])
        .size()
        .reset_index(name="Shipment Count")
        .sort_values(by="Shipment Count", ascending=False)
    )

    print(result.head(10))
    return result


def shipment_mode_by_country(df):
    """Return shipment count by country and shipment mode."""
    print("\n--- SHIPMENT MODE BY COUNTRY ---")
    result = (
        df.groupby(["Country", "Shipment Mode"])
        .size()
        .reset_index(name="Shipment Count")
        .sort_values(by="Shipment Count", ascending=False)
    )

    print(result.head(10))
    return result


def plot_bar_chart(series, title):
    """
    Create and return a matplotlib bar chart.
    This can be reused later in Streamlit or another visualization tool.
    """
    fig, ax = plt.subplots()

    series.plot(kind="bar", ax=ax)

    ax.set_title(title)
    ax.set_xlabel("Category")
    ax.set_ylabel("Count")

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


if __name__ == "__main__":
    import os
    import sys

    # Force Python to read from the current directory folder
    current_folder = os.path.dirname(os.path.abspath(__file__))
    if current_folder not in sys.path:
        sys.path.insert(0, current_folder)

    # Import your transformed dataframe
    try:
        from data_transformation import df as transformed_df
        df = transformed_df
        print("[SUCCESS] Successfully connected to Member 3's pipeline!")
    except ModuleNotFoundError:
        print("[ERROR] Could not find data_transformation.py in this folder.")
        df = None

    # Run her analytical functions
    if df is not None:
        basic_info(df)
        print(missing_values_summary(df))
        print(summary_statistics(df))
        
        top_countries = top_countries_by_records(df, 10)
        fig = plot_bar_chart(top_countries, "Top 10 Countries by Shipment Records")
        plt.show()