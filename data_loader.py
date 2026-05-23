import pandas as pd

def load_supply_data(file_path):

    try:
        df = pd.read_csv(file_path)

        print("Dataset loaded successfully.")
        print("Rows:", df.shape[0])
        print("Columns:", df.shape[1])

        return df

    except FileNotFoundError:
        print("Error: File path not found.")

    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")

    except Exception as e:
        print("Unexpected error:", e)
