import pandas as pd
import numpy as np


try:
    df = pd.read_csv('Bengaluru Ola.csv', on_bad_lines='skip', engine='python')
    print("Data loaded successfully!")
    
    # Strip any leading/trailing whitespace from all column names
    df.columns = df.columns.str.strip()
    
    print("\n--- Columns in the DataFrame ---")
    print(df.columns)
    
    print("\n--- Missing Value Counts ---")
    print(df.isnull().sum())
    
except FileNotFoundError:
    print("Error: 'Bengaluru Ola.csv' not found. Please check your file path.")