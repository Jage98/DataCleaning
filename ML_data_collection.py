

import os
import pandas as pd
import matplotlib.pyplot as plt
import uuid  

# Set the folder path containing your CSV files
folder_path = 'YourPathHere'

# List of columns to plot
columns_to_plot = ['YourColumn']  # Replace with the column names you want to visualize

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Loop through each CSV file
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path)

    # Check if all specified columns exist in the DataFrame
    missing_columns = [col for col in columns_to_plot if col not in df.columns]
    if missing_columns:
        print(f"Columns {missing_columns} not found in {csv_file}. Skipping this file.")
        continue

    # Plot the data
    plt.figure()
    for col in columns_to_plot:
        plt.plot(df[col], label=col)
    plt.title(f"Select start and end points for {csv_file}")
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    print(f"Plotting {csv_file}. Please click on the plot to select start and end points.")

    # Use ginput to get two points from the user
    points = plt.ginput(2, timeout=-1)  # Wait indefinitely until two clicks are received
    plt.close()

    # Ensure two points were selected
    if len(points) != 2:
        print(f"Insufficient points selected for {csv_file}. Skipping this file.")
        continue

    # Extract the x-coordinates (indices)
    start_index = int(round(points[0][0]))
    end_index = int(round(points[1][0]))

    # Ensure start_index is less than end_index
    if start_index >= end_index:
        print(f"Invalid selection for {csv_file}. Start index is not less than end index.")
        continue

    # Crop the DataFrame
    cropped_df = df.iloc[start_index:end_index]

    # Generate a unique filename for the cropped file
    unique_id = uuid.uuid4()
    cropped_file_name = f"{unique_id}.csv"
    cropped_file_path = os.path.join('YourNewFolder', cropped_file_name) # your actual folder where you want the cropped files to be saved

    # Save the cropped data to the new CSV file
    cropped_df.to_csv(cropped_file_path, index=False)
    print(f"Cropped data saved to {cropped_file_name}")

print("Processing complete.")
