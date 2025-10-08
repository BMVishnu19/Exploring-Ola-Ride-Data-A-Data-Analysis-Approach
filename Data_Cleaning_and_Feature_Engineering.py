import pandas as pd
import numpy as np


def clean_and_engineer_data(file_path):
    """
    Loads a CSV file, cleans the data, and adds new engineered features.
    
    Args:
        file_path (str): The path to the CSV file.
    
    Returns:
        pandas.DataFrame: The cleaned DataFrame with new features.
    """
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
        print("Data loaded successfully!")
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found. Please check your file path.")
        return None

    
    df.columns = df.columns.str.strip()

   
    df['Date_Time'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df.drop(['Date', 'Time'], axis=1, inplace=True)

   
    numeric_cols = ['Avg VTAT', 'Avg CTAT', 'Ride Distance', 'Booking Value', 'Driver Ratings', 'Customer Rating']
    df[numeric_cols] = df[numeric_cols].fillna(0)

    
    categorical_cols = ['Reason for Cancelling by Customer', 'Reason for Cancelling by Driver', 'Incomplete Rides Reason', 'Payment Method']
    for col in ['Reason for Cancelling by Customer', 'Reason for Cancelling by Driver']:
        df[col].fillna('Not Cancelled', inplace=True)
    df['Incomplete Rides Reason'].fillna('Not Applicable', inplace=True)
    df['Payment Method'].fillna('Not Applicable', inplace=True)

    print("\nData cleaning complete!")
    print("\n--- Final Data Information ---")
    df.info()

    
    df['Day_of_Week'] = df['Date_Time'].dt.day_name()
    df['Hour_of_Day'] = df['Date_Time'].dt.hour
    df['Month'] = df['Date_Time'].dt.month_name()
    df['Is_Weekend'] = df['Day_of_Week'].isin(['Saturday', 'Sunday']).astype(int)

    
    df['Is_Cancelled'] = df['Booking Status'].apply(lambda x: 1 if 'Cancelled' in x else 0)

    
    df['Cost_Per_KM'] = df['Booking Value'] / df['Ride Distance']
    df['Cost_Per_KM'].replace([np.inf, -np.inf], 0, inplace=True)

    print("\nFeature engineering complete!")
    print("\n--- Snapshot of Final DataFrame ---")
    print(df.head())

    return df


if __name__ == "__main__":
    file_path = 'Bengaluru Ola.csv'
    final_df = clean_and_engineer_data(file_path)

    if final_df is not None:
        output_file_path = 'advanced_bengaluru_ola_dataset.csv'
        final_df.to_csv(output_file_path, index=False)
        print(f"\nAdvanced dataset saved successfully to {output_file_path}")