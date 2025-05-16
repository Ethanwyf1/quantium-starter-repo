import pandas as pd
import os
import glob

# Define input and output paths
data_dir = "data/"
output_dir = "output/"
output_file = "formatted_data.csv"
output_path = os.path.join(output_dir, output_file)

# Get all CSV files in the data directory
file_paths = glob.glob(os.path.join(data_dir, "daily_sales_data_*.csv"))

# Container for processed data
all_data = []

# Process each file
for file_path in file_paths:
    df = pd.read_csv(file_path)
    print("📄 Processing file:", file_path)
    print("🔑 Original columns:", df.columns.tolist())
    print("📊 Total rows before filtering:", len(df))

    # Clean up column names
    df.columns = df.columns.str.strip()

    # Strip whitespace and lowercase for comparison
    df["product"] = df["product"].str.strip()
    print("🧪 Unique product values:", df["product"].unique())

    # Filter for Pink Morsel product only (case insensitive)
    df = df[df["product"].str.lower() == "pink morsel"]
    print("🎯 Rows after filtering for 'Pink Morsel':", len(df))

    # Remove $ from price and convert to float
    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

    # Calculate sales
    df["sales"] = df["price"] * df["quantity"]

    # Select relevant columns
    df_clean = df[["sales", "date", "region"]]

    # Append to list
    all_data.append(df_clean)

# Concatenate all cleaned data
final_df = pd.concat(all_data, ignore_index=True)
print("✅ Final row count after merging all files:", len(final_df))

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# If output file exists, remove it to avoid PermissionError
if os.path.exists(output_path):
    try:
        os.remove(output_path)
        print(f"🧹 Removed existing file: {output_path}")
    except PermissionError:
        print(f"❌ Permission denied: please close '{output_path}' and run again.")
        exit(1)

# Save the result
final_df.to_csv(output_path, index=False)
print("📁 Output saved to:", output_path)