import csv
import os

# Directory containing the input data
DATA_DIRECTORY = "./data"

# Path to the output file
OUTPUT_FILE_PATH = "./formatted_data.csv"

# Open the output file for writing formatted data
with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)

    # Write CSV header row
    header = ["sales", "date", "region"]
    writer.writerow(header)

    # Iterate through all CSV files in the data directory
    for file_name in os.listdir(DATA_DIRECTORY):
        # Open each file for reading
        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            row_index = 0

            # Iterate through each row
            for input_row in reader:
                # Skip the header row
                if row_index > 0:
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    transaction_date = input_row[3]
                    region = input_row[4]

                    # Process only records for pink morsel
                    if product == "pink morsel":
                        # Remove the $ symbol and convert to float
                        price = float(raw_price[1:])
                        # Calculate the sales amount for the row
                        sale = price * int(quantity)

                        # Write the structured data row
                        output_row = [sale, transaction_date, region]
                        writer.writerow(output_row)
                row_index += 1
