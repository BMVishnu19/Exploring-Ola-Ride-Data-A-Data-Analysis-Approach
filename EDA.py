import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


try:
    df = pd.read_csv('advanced_bengaluru_ola_dataset.csv')
    print("Cleaned dataset loaded successfully for EDA.")
except FileNotFoundError:
    print("Error: The 'advanced_bengaluru_ola_dataset.csv' file was not found. Please run the previous data cleaning script first.")

# Setting the style for plots
sns.set_style("whitegrid")
plt.style.use('seaborn-v0_8-darkgrid')

# --- 1. Distribution of Booking Status ---
print("\n--- Plotting Distribution of Booking Status ---")
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Booking Status', palette='viridis')
plt.title('Distribution of Booking Status')
plt.xlabel('Booking Status')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.show()


# --- 2. Busiest Hours of the Day ---
print("\n--- Plotting Busiest Hours of the Day ---")
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Hour_of_Day', order=df['Hour_of_Day'].value_counts().index, palette='plasma')
plt.title('Number of Bookings by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Bookings')
plt.show()


# --- 3. Busiest Days of the Week ---
print("\n--- Plotting Busiest Days of the Week ---")
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Day_of_Week', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='cividis')
plt.title('Number of Bookings by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Bookings')
plt.show()


# --- 4. Cancellation Reasons by Customer ---
print("\n--- Plotting Top 10 Customer Cancellation Reasons ---")
customer_cancellation_reasons = df[df['Is_Cancelled'] == 1]['Reason for Cancelling by Customer'].value_counts().head(10)
plt.figure(figsize=(12, 7))
sns.barplot(x=customer_cancellation_reasons.values, y=customer_cancellation_reasons.index, palette='coolwarm')
plt.title('Top 10 Reasons for Cancellation by Customers')
plt.xlabel('Number of Cancellations')
plt.ylabel('Reason')
plt.show()


# --- 5. Cancellation Reasons by Driver ---
print("\n--- Plotting Top 10 Driver Cancellation Reasons ---")
driver_cancellation_reasons = df[df['Is_Cancelled'] == 1]['Reason for Cancelling by Driver'].value_counts().head(10)
plt.figure(figsize=(12, 7))
sns.barplot(x=driver_cancellation_reasons.values, y=driver_cancellation_reasons.index, palette='magma')
plt.title('Top 10 Reasons for Cancellation by Drivers')
plt.xlabel('Number of Cancellations')
plt.ylabel('Reason')
plt.show()