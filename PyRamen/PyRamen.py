# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# Import libraries
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Read in the menu data into the menu list
with open(menu_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #  skip header
    header = next(csvreader)

    for row in csvreader:
        
        price = float(row[3])
        cost = float(row[4])
        menu.append(
            {
                # "id": row[0],
                "item": row[0],
                "category": row[1],
                "description": row[2],
                "price": price,
                "cost": cost,
                "profit": price - cost,
            }
        )


# Read in the sales data into the sales list
with open(sales_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #  skip header
    header = next(csvreader)

    for row in csvreader:
        sales.append(
            {
                "id": row[0],
                "date": row[1],
                "credit_card_number": row[2],
                "quantity": int(row[3]),
                "menu_item": row[4],
            }
        )

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# Loop over every row in the sales list object

for sale in sales:
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # Initialize sales data variables
    quantity = sale['quantity']
    sales_item = sale['menu_item']
    #
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit

    if report.get(sales_item) is None:
        report[sales_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }

    # For every row in our sales data, loop over the menu records to determine a match
    menu_item_dict = {}
    for item in menu:
        if item['item'] == sales_item:
            menu_item_dict = item
    
        # Item,Category,Description,Price,Cost
        # Initialize menu data variables
    report[sales_item]["01-count"] += quantity
    
        # Calculate profit of each item in the menu data


        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
    if bool(menu_item_dict):
        # Print out matching menu data
        # Cumulatively add up the metrics for each item key
        report[sales_item]["02-revenue"] += menu_item_dict['price'] * quantity
        report[sales_item]["03-cogs"] += menu_item_dict['cost'] * quantity
        report[sales_item]["04-profit"] += menu_item_dict['profit'] * quantity
        
    else:
    # Else, the sales item does not equal any fo the item in the menu data, therefore no match
        print("No match")

    # Increment the row counter by 1
    row_count += 1

# Print total number of records in sales data
print(f"Total records in sale data {row_count}")

# Write out report to a text file (won't appear on the command line output)
# Set the path for the output.csv
output = Path("output.csv")

print(report)
# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','
with open(output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Menu item", "01-count", "02-revenue", "03-cogs", "04-profit"])
    # Loop through the list of records and write every record to the
    # output csv file
    for menu_item, record in report.items():
        csvwriter.writerow([menu_item, record["01-count"], record["02-revenue"], record["03-cogs"], record["04-profit"]])

