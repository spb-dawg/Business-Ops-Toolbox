import csv
from collections import defaultdict

def calculate_burn(input_file):
    category_totals = defaultdict(float)
    total_burn = 0

    try:
        with open(input_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                amount = float(row['amount'])
                category = row['category'].strip().title()
                
                category_totals[category] += amount
                total_burn += amount

        print("--- Monthly Burn Report ---")
        for cat, total in category_totals.items():
            print(f"{cat}: ${total:,.2f}")
        print("---------------------------")
        print(f"TOTAL MONTHLY BURN: ${total_burn:,.2f}")
        
    except FileNotFoundError:
        print("Error: expense_report.csv not found.")

# run the calculation
# calculate_burn('expense_report.csv')
