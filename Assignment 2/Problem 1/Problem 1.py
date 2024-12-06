import sqlite3
import csv

print("Customer Data Importer\n")

csv_file_path = input("CSV File: ")
db_file_path = input("DB File: ")
table_name = input("Table name: ")

conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

create_table_query = f'''
CREATE TABLE IF NOT EXISTS {table_name} (
    customerID INTEGER PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    companyName TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT
)
'''

cursor.execute(create_table_query)

cursor.execute(f'DELETE FROM {table_name}')
print(f"\nAll old rows deleted from {table_name} table.")

with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    rows = [(row['first_name'], row['last_name'], row['company_name'], row['address'], row['city'], row['state'], row['zip']) for row in csv_reader]
    
    insert_query = f'''
    INSERT INTO {table_name} (firstName, lastName, companyName, address, city, state, zip)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    
    cursor.executemany(insert_query, rows)
    print(f"{len(rows)} row(s) inserted into {table_name} table.")

conn.commit()
conn.close()
