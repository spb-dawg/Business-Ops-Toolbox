import csv

def clean_data(input_file, output_file):
    seen_emails = set()
    cleaned_rows = []

    with open(input_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 1. Basic Cleaning: Remove whitespace
            email = row['email'].strip().lower()
            
            # 2. De-duplication Logic
            if email not in seen_emails and email != "":
                seen_emails.add(email)
                
                # 3. Data Transformation (e.g., capitalizing names)
                row['name'] = row['name'].title()
                row['email'] = email
                
                cleaned_rows.append(row)

    # 4. Save the "Professional" version
    keys = cleaned_rows[0].keys()
    with open(output_file, 'w', newline='') as output:
        dict_writer = csv.DictWriter(output, keys)
        dict_writer.writeheader()
        dict_writer.writerows(cleaned_rows)
    
    print(f"Success! Cleaned {len(cleaned_rows)} unique records.")

# To run this, you'd just need a CSV file named 'raw_leads.csv'
# clean_data('raw_leads.csv', 'cleaned_leads.csv')
